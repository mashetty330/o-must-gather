import os
import sys

from omg.common.config import Config
from omg.common.helper import load_yaml_file


def check_flexible(files_to_check, show_output=True):

    files = [f for f in files_to_check.split(",")]
    mg_path = Config().path
    yaml_path = os.path.join(mg_path, files[0])
    print("This feature yet to be completed!!")


def check_connected(files_to_check, show_output=True):

    files = [f for f in files_to_check.split(",")]
    mg_path = Config().path

    yaml_dir_path = os.path.join(mg_path, files[0])
    files_in_dir = os.listdir(yaml_dir_path)
    yaml_path = ""

    for file in files_in_dir:
        if "ocs-operator" in str(file) and file.endswith(".yaml"):
            yaml_path = os.path.join(yaml_dir_path, file)
    try:
        res = load_yaml_file(yaml_path, print_warnings=True)
    except Exception as err:
        print(f"[ERROR] File {yaml_path} can't be opened: {err}")
        sys.exit(1)
    str_to_check = "quay.io/rhceph-dev/"
    status = ''
    try:
        if res["metadata"]:
            res = res["metadata"]
            if res["annotations"]:
                res = res["annotations"]
                if res["containerImage"]:
                    res = res["containerImage"]
                    if str_to_check in str(res):
                        status = "connected"
                    else:
                        status = "disconnected"
                else:
                    print("[ERROR] Unexpected error while checking. Error at containerImage")
                    status = -1
            else:
                print("[ERROR] Unexpected error while checking. Error at annotations")
                status = -1
        else:
            print("[ERROR] Unexpected error while checking. Error at metadata")
            status = -1
    except Exception as err:
        print(f"[ERROR] Unexpected error: {err}")

    if status == -1:
        sys.exit(1)
    elif show_output:
        print(status)
    else:
        return status


def check_noobaa(files_to_check, show_output=True):

    files = [f for f in files_to_check.split(",")]
    mg_path = Config().path
    yaml_path = os.path.join(mg_path, files[0])

    file_exists = os.path.exists(yaml_path)
    if not file_exists:
        status = "No info available!!"
        if show_output:
            print(status)
        else:
            return status

    try:
        res = load_yaml_file(yaml_path, print_warnings=True)
    except Exception as err:
        print(f"[ERROR] File {yaml_path} can't be opened: {err}")
        sys.exit(1)

    status = ''
    if "items" in res:
        if res["items"] is not None and len(res["items"]) > 0:
            res = res["items"][0]
        else:
            print("[ERROR] Unexpected error while checking")
            status = -1

    if "status" in res and status != -1:
        res = res["status"]
        if "images" in res:
            res = res["images"]
            if "noobaaCore" in res and "noobaaDB" in res:
                status = "Nooba enabled"
            else:
                status = "Nooba disabled"
                #print("[ERROR] Unexpected error while checking")
        else:
            status = -1
            print("[ERROR] Unexpected error while checking")
    else:
        status = -1
        print("[ERROR] Unexpected error while checking")

    if status == -1:
        sys.exit(1)
    elif show_output:
        print(status)
    else:
        return status


def check_external(files_to_check, show_output=True):

    files = [f for f in files_to_check.split(",")]
    mg_path = Config().path
    yaml_path = os.path.join(mg_path, files[0])

    file_exists = os.path.exists(yaml_path)
    if not file_exists:
        status = "No info available!!"
        if show_output:
            print(status)
        else:
            return status
    try:
        res = load_yaml_file(yaml_path, print_warnings=True)
    except Exception as err:
        print(f"[ERROR] File {yaml_path} can't be opened: {err}")
        sys.exit(1)

    status = ""
    if "items" in res:
        if res["items"] is not None and len(res["items"]) > 0:
            res = res["items"][0]
        else:
            print("[ERROR] Unexpected error while checking")
            status = -1

    if "spec" in res and status != -1:
        res = res["spec"]
        if "externalStorage" in res:
            res = res["externalStorage"]
            if "enable" in res:
                res = res["enable"]
                if res == "true":
                    status = "External"
                else:
                    status = "Internal"
            else:
                status = "Internal"
        else:
            status = -1
            print("[ERROR] Can't check if the cluster is External!")
    else:
        status = -1
        print("[ERROR] Unexpected error while checking")

    if status == -1:
        sys.exit(1)
    elif show_output:
        print(status)
    else:
        return status


def check_lso(files_to_check, show_output=True):
    files = [f for f in files_to_check.split(",")]
    mg_path = Config().path
    yaml_path = os.path.join(mg_path, files[0])

    yamls = []

    if os.path.isdir(yaml_path):
        yamls.extend(
            [os.path.join(yaml_path, y) for y in os.listdir(yaml_path) if y.endswith(".yaml")]
        )
    else:
        print("[ERROR] Some unexpected error occured!!")
        sys.exit(1)

    status = 0
    for y in yamls:

        try:
            res = load_yaml_file(y, print_warnings=True)
        except Exception as err:
            print(f"[ERROR] File {y} can't be opened: {err}")
            sys.exit(1)

        if "spec" in res:
            res = res["spec"]
            if "storageClassName" in res:
                res = res["storageClassName"]
                if res == "localblock":
                    status = 1
                else:
                    continue
            else:
                status = -1
                continue
        else:
            status = -1
            continue

        if status == 1:
            break

    output = ''
    if status == -1:
        print("[ERROR] Unexepcted error! couldn't check if cluster has local storage!!")
        sys.exit(1)
    elif status == 0:
        output = "No, doesnt have local storage"
    elif status == 1:
        output = "Yes, has local storage"
    if show_output:
        print(output)
    else:
        return output


def check_ipi_upi(files_to_check, show_output=True):
    files = [f for f in files_to_check.split(",")]
    mg_path = Config().path
    yaml_path = os.path.join(mg_path, files[0])
    file_exists = os.path.exists(yaml_path)

    output = ""
    if "quay-io-rhceph-dev-ocs-must-gather" in mg_path:
        output = "No info available to check if the cluster is IPI/UPI in the OCS Must-Gather"
        if show_output:
            print(output)
            sys.exit(1)
        else:
            return output

    if os.path.isdir(yaml_path):
        if len(os.listdir(yaml_path)) > 0:
            output = "IPI"
        else:
            output = "UPI"
    else:
        output = "UPI"

    if show_output:
        print(output)
    else:
        return output


