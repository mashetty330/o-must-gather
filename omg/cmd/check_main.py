import sys

from omg.cmd.check.check_method import check_flexible, check_connected, check_noobaa, check_external, check_lso

check_map = [
    {
        "something": "flexible",
        "where_file": "namespaces/openshift-storage/oc_output/storagecluster.yaml",
        "how_func": check_flexible,
    },
    {
        "something": "connected",
        "where_file": "namespaces/openshift-storage/operators.coreos.com/clusterserviceversions/ocs-operator.v4.10.0.yaml",
        "how_func": check_connected,
    },
    {
        "something": "noobaa",
        "where_file": "namespaces/openshift-storage/oc_output/storagecluster.yaml",
        "how_func": check_noobaa,
    },
    {
        "something": "external",
        "where_file": "namespaces/openshift-storage/oc_output/storagecluster.yaml",
        "how_func": check_external,
    },
    {
        "something": "lso",
        "where_file": "cluster-scoped-resources/core/persistentvolumes",
        "how_func": check_lso,
    },

]


def get_info_dict(something):
    for item in check_map:
        if item["something"] == something:
            return item
    return None


def check(something, show_output=True):
    if len(something) == 0:
        print("you gotta check for something! :)")
        sys.exit(1)
    info_dict = get_info_dict(something[0])
    if not info_dict:
        print(f"[ERROR] to check if {something[0]}, feature isn't implemented yet!")
        sys.exit(1)

    out_func = info_dict["how_func"]
    out = out_func(info_dict["where_file"], show_output=show_output)
    if not show_output:
        return out
