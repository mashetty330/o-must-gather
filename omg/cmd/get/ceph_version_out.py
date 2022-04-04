# -*- coding: utf-8 -*-
from tabulate import tabulate

from omg.common.helper import age


# SCV out put with just name and version
def ceph_version_out(t, ns, res, output, show_type, show_labels, show_output):
    output_res = [[]]
    # header
    #if ns == "_all":
        #output_res[0].append("NAMESPACE")
    output_res[0].extend(["VERSION"])
    # resources
    for r in res:
        keys = list(r.keys())
        try:
            version = r["version"]
        except Exception as err:
            version = r[keys[1]]
        row = []
        # namespace (for --all-namespaces)
        #if ns == "_all":
        #    row.append(p["metadata"]["namespace"])
        # name
        if show_type:
            version = t + "/" + version
        # version
        try:
            row.append(version)
        except:
            row.append("Unknown")

        output_res.append(row)
    if show_output:
        print(tabulate(output_res, tablefmt="plain"))
    return output_res
