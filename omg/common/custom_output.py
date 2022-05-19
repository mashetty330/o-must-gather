from tabulate import tabulate
from omg.cmd.get_main import get_main
from omg.cmd.get_main import get_main
from omg.cmd.check_main import check

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
                "func": "get_main",
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
                "func": "get_main",
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
                "func": "get_main",
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
                "func": "get_main",
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
                "func": "get_main",
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
                "func": "get_main",
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
                "func": "get_main",
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
                "func": "get_main",
            },
            {
                "name": ("noobaa",),
                "custom_str": "Is Noobaa enabled?",
                "intermediate_str": " ",
                "func": "check",
            },
            {
                "name": ("connected",),
                "custom_str": "Is cluster connected/disconnected?",
                "intermediate_str": None,
                "func": "check",
            },
            {
                "name": ("external",),
                "custom_str": "Is cluster Internal/External?",
                "intermediate_str": None,
                "func": "check",
            },
            {
                "name": ("lso",),
                "custom_str": "Does cluster have local storage?",
                "intermediate_str": None,
                "func": "check",
            },
            {
                "name": ("ipi",),
                "custom_str": "Is cluster IPI/UPI?",
                "intermediate_str": None,
                "func": "check",
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
                "func": "get_main",
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
        int_str = r["intermediate_str"]
        if int_str:
            print(f"{int_str}")
        c_str = r["custom_str"]
        func = r["func"]
        if func == "get_main":
            out = get_main(objects=r["name"],
                           output=r["output"],
                           namespace=r["namespace"],
                           all_namespaces=r["all_namespaces"],
                           show_labels=r["show_labels"],
                           show_output=r["show_output"],
                           count=r["count"])
            if not out:
                out = "No info available!!"
                print(f"{c_str}: {out}")
                continue
            key = r["key"]
            if r["count"]:
                print(f"{c_str}: {out}")
            elif key is not None:
                print(f"{c_str}: {out[1][key]}")
            else:
                print(f"{c_str}:")
                print(tabulate(out, headers="firstrow", tablefmt="orgtbl"))
        elif func == "check":
            out = check(something=r["name"], show_output=False)
            if not out:
                out = "No info available!!"
            print(f"{c_str}: {out}")
    print()
