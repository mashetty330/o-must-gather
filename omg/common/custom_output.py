from tabulate import tabulate
from omg.cmd.get_main import get_main

custom_map = [
    {
        "type": "storageclusterdetails",
        "alias": ["scd", "storagedetails", "ocsclusterdetails", "ocsdetails"],
        "resources": [
            {
                "name": ("platform",),
                "output": None,
                "namespace": None,
                "all_namespaces": False,
                "show_labels": False,
                "count": False,
                "show_output": False,
                "custom_str": "Platform",
                "intermediate_str": None,
                "key": 1,
            },
            {
                "name": ("scv",),
                "output": None,
                "namespace": "openshift-storage",
                "all_namespaces": False,
                "show_labels": False,
                "count": False,
                "show_output": False,
                "custom_str": "OCS version",
                "intermediate_str": "\n----VERSIONS----",
                "key": 1,
            },
            {
                "name": ("ocv",),
                "output": None,
                "namespace": None,
                "all_namespaces": False,
                "show_labels": False,
                "count": False,
                "show_output": False,
                "custom_str": "OCP version",
                "intermediate_str": None,
                "key": 1,
            },
            {
                "name": ("cv",),
                "output": None,
                "namespace": "openshift-storage",
                "all_namespaces": False,
                "show_labels": False,
                "count": False,
                "show_output": False,
                "custom_str": "Ceph version",
                "intermediate_str": None,
                "key": 0,
            },
            {
                "name": ("scs",),
                "output": None,
                "namespace": "openshift-storage",
                "all_namespaces": False,
                "show_labels": False,
                "count": False,
                "show_output": False,
                "custom_str": "Cluster encryption",
                "intermediate_str": "\n----SECURITY----",
                "key": 1,
            },
            {
                "name": ("nodes",),
                "output": None,
                "namespace": None,
                "all_namespaces": False,
                "show_labels": False,
                "count": True,
                "show_output": False,
                "custom_str": "Number of Nodes",
                "intermediate_str": " ",
                "key": None,
            },
            {
                "name": ("pvc",),
                "output": None,
                "namespace": "openshift-storage",
                "all_namespaces": False,
                "show_labels": False,
                "count": True,
                "show_output": False,
                "custom_str": "Number of PVCs",
                "intermediate_str": None,
                "key": None,
            },
            {
                "name": ("osd",),
                "output": None,
                "namespace": "openshift-storage",
                "all_namespaces": False,
                "show_labels": False,
                "count": True,
                "show_output": False,
                "custom_str": "Number of OSDs",
                "intermediate_str": None,
                "key": None,
            },
            {
                "name": ("node-details",),
                "output": None,
                "namespace": None,
                "all_namespaces": False,
                "show_labels": False,
                "count": False,
                "show_output": False,
                "custom_str": "Node details",
                "intermediate_str": " ",
                "key": None,
            },
        ],
        "custom_str": "STORAGE CLUSTER DETAILS",
    },
]


def check_if_custom(objects):
    for x in custom_map:
        if objects[0] == x["type"] or objects[0] in x["alias"]:
            return x
        else:
            return None


def print_custom_output(r_dict, objects):

    print()
    r_name = ""
    fill = "-----------------------"
    if len(objects) > 1:
        r_name = f" [{objects[1]}]"
    r_type = r_dict["type"]
    r_list = r_dict["resources"]
    try:
        custom_str = r_dict["custom_str"]
    except:
        custom_str = None

    if custom_str is not None:
        print(f"{fill}{custom_str}{r_name}{fill}\n")
    else:
        print(f"{fill}{r_type}{r_name}{fill}\n")
    for r in r_list:
        int_str=r["intermediate_str"]
        if int_str:
            print(f"{int_str}")
        key = r["key"]
        c_str = r["custom_str"]
        out = get_main(objects=r["name"], output=r["output"], namespace=r["namespace"], all_namespaces=r["all_namespaces"], show_labels=r["show_labels"], show_output=r["show_output"], count=r["count"])
        if r["count"]:
            print(f"{c_str}: {out}")
        elif key is not None:
            print(f"{c_str}: {out[1][key]}")
        else:
            print(f"{c_str}:")
            print(tabulate(out, headers="firstrow", tablefmt="orgtbl"))

    print()
