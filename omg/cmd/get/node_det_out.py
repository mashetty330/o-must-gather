# -*- coding: utf-8 -*-
from tabulate import tabulate

from omg.common.helper import age


# SCV out put with just name and version
def node_det_out(t, ns, res, output, show_type, show_labels, show_output):
    output_res = [[]]
    # header
    #if ns == "_all":
        #output_res[0].append("NAMESPACE")
    output_res[0].extend(["NAME", "ARCHITECTURE", "KERNEL VERSION", "OPERATING SYSTEM", "OS IMAGE"])
    # resources
    for r in res:
        keys = list(r.keys())
        try:
            name = r["name"]
        except Exception as err:
            name = r[keys[0]]
        try:
            kernelVersion = r["kernelVersion"]
        except Exception as err:
            kernelVersion = r[keys[1]]

        try:
            architecture = r["architecture"]
        except Exception as err:
            architecture = r[keys[1]]

        try:
            operatingSystem = r["operatingSystem"]
        except Exception as err:
            operatingSystem = r[keys[1]]

        try:
            osImage = r["osImage"]
        except Exception as err:
            osImage = r[keys[1]]


        row = []
        # namespace (for --all-namespaces)
        #if ns == "_all":
        #    row.append(p["metadata"]["namespace"])
        # name
        if show_type:
            row.append(t + "/" + name)
        else:
            row.append(name)

        row.append(architecture)
        row.append(kernelVersion)
        row.append(operatingSystem)
        row.append(osImage)
        output_res.append(row)
    if show_output:
        print(tabulate(output_res, tablefmt="plain"))
    return output_res
