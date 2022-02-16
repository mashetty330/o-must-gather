# -*- coding: utf-8 -*-
from tabulate import tabulate

from omg.common.helper import age


# SCV out put with just name and version
def scv_out(t, ns, res, output, show_type, show_labels):
    output_res = [[]]
    # header
    #if ns == "_all":
        #output_res[0].append("NAMESPACE")
    output_res[0].extend(["NAME", "VERSION"])
    # resources
    for r in res:
        keys = list(r.keys())
        try:
            name = r["name"]
        except Exception as err:
            name = r[keys[0]]
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
            row.append(t + "/" + name)
        else:
            row.append(name)
        # version
        try:
            row.append(version)
        except:
            row.append("Unknown")

        output_res.append(row)

    print(tabulate(output_res, tablefmt="plain"))
