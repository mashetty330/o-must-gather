import re


def get_count(r_type, res, show_output):
    count = 0
    for resource in res:
        r = resource["res"]
        name = r["metadata"]["name"]
        if r_type == "osd" and not re.match(r'^rook-ceph-osd-[0-9]+', name):
            continue
        count += 1
    if show_output:
        print("Number of {}: {}".format(r_type, count))
    return True, count
