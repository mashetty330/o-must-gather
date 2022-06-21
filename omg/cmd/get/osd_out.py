# -*- coding: utf-8 -*-
import re

from tabulate import tabulate
from omg.common.helper import age, extract_labels


# Special function to output pod
# Generate output table if -o not set or 'wide'
# We will create an array of array and then print if with tabulate
def osd_out(t, ns, res, output, show_type, show_labels, show_output):
    output_pods = [[]]
    # header
    if ns == "_all":
        output_pods[0].append("NAMESPACE")
    if output == "wide" and not show_labels:
        output_pods[0].extend(
            ["NAME", "READY", "STATUS", "RESTARTS", "AGE", "IP", "NODE"]
        )
    elif output == "wide" and show_labels:
        output_pods[0].extend(
            ["NAME", "READY", "STATUS", "RESTARTS", "AGE", "IP", "NODE", "LABELS"]
        )
    elif show_labels:
        output_pods[0].extend(["NAME", "READY", "STATUS", "RESTARTS", "AGE", "LABELS"])
    else:
        output_pods[0].extend(["NAME", "READY", "STATUS", "RESTARTS", "AGE"])
    # pods
    for pod in res:
        p = pod["res"]
        row = []
        name = p["metadata"]["name"]
        if not re.match(r'^rook-ceph-osd-[0-9]+', name):
            continue
        # namespace (for --all-namespaces)
        if ns == "_all":
            row.append(p["metadata"]["namespace"])
        # name
        if show_type:
            row.append(t + "/" + name)
        else:
            row.append(name)
        # containers/ready count
        if "containers" in p["spec"]:
            containers = str(len(p["spec"]["containers"]))
        else:
            containers = "0"
        if "containerStatuses" in p["status"]:
            containers_ready = str(
                len([r for r in p["status"]["containerStatuses"] if r["ready"] is True])
            )
            restarts = max(
                [r["restartCount"] for r in p["status"]["containerStatuses"]]
            )
        else:
            containers_ready = "0"
            restarts = 0
        row.append(containers_ready + "/" + containers)
        # status
        row.append(p["status"]["phase"])
        # restarts
        row.append(restarts)
        # age
        pod_ct = str(p["metadata"]["creationTimestamp"])
        gen_ts = pod["gen_ts"]
        row.append(age(pod_ct, gen_ts))
        # pod ip and node (if -o wide)
        if output == "wide":
            if "podIP" in p["status"]:
                row.append(p["status"]["podIP"])
            else:
                row.append("")
            if "nodeName" in p["spec"]:
                row.append(p["spec"]["nodeName"])
            else:
                row.append("")
        # show-labels
        if show_labels:
            row.append(extract_labels(p))

        output_pods.append(row)

    if show_output:
        print(tabulate(output_pods, tablefmt="plain"))
    return output_pods

