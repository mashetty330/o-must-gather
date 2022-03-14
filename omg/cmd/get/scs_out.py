# -*- coding: utf-8 -*-
from tabulate import tabulate

from omg.common.helper import age


# SCV out put with just name and version
def scs_out(t, ns, res, output, show_type, show_labels, show_output):
    output_res = [[]]
    # header
    #if ns == "_all":
        #output_res[0].append("NAMESPACE")
    output_res[0].extend(["NAME", "SECURITY"])
    scs = []
    # resources
    for r in res:
        keys = list(r.keys())
        try:
            name = r["name"]
        except Exception as err:
            name = r[keys[0]]
        try:
            security = r["encryption"]
        except Exception as err:
            security = r[keys[1]]
        scs.append(security)
        row = []
        # namespace (for --all-namespaces)
        #if ns == "_all":
        #    row.append(p["metadata"]["namespace"])
        # name
        if show_type:
            row.append(t + "/" + name)
        else:
            row.append(name)
        # version
        try:
            row.append(security)
        except:
            row.append("Unknown")

        output_res.append(row)
    if show_output:
        print(tabulate(output_res, tablefmt="plain"))
    return scs