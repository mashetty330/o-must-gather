
from omg.cmd.get_main import get_main

def get_storage_details():

    #fetch all the storage details and output

    #get platform details
    print("\nSTORAGE CLUSTER DETAILS:")

    platform = get_main(("platform",), namespace=None, all_namespaces=False, output=None, show_labels=False, count=False, show_output=False)
    print("Platform: {}".format(platform[0]))

    sc_version = get_main(("scv",), namespace="openshift-storage", all_namespaces=False, output=None, show_labels=False, count=False, show_output=False)
    print("OCS version: {}".format(sc_version[0]))

    ocp_version = get_main(("ocv",), namespace=None, all_namespaces=False, output=None, show_labels=False,
                          count=False, show_output=False)
    print("OCP version: {}".format(ocp_version[0]))

    cluster_encr = get_main(("scs",), namespace="openshift-storage", all_namespaces=False, output=None, show_labels=False, count=False, show_output=False)
    print("Cluster encryption: {}".format(cluster_encr[0]))

    print()

    n_nodes = get_main(("nodes",), namespace=None, all_namespaces=False, output=None, show_labels=False, count=True, show_output=False)
    print("Number of Nodes: {}".format(n_nodes))

    n_pvcs = get_main(("pvc",), namespace="openshift-storage", all_namespaces=False, output=None, show_labels=False, count=True, show_output=False)
    print("Number of PVC: {}".format(n_pvcs))

    n_osds = get_main(("osd",), namespace="openshift-storage", all_namespaces=False, output=None, show_labels=False, count=True, show_output=False)
    print("Number of OSD: {}".format(n_osds))

    print()