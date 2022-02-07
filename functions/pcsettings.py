import time, datetime, json, psutil
from misc_functions.bcolors import bcolors





with open("oc.json", "r") as fp:
    data = json.load(fp)

options = [""]


def pcoperation():
    for option in options:
        pc_on = data["PC_STATUS"]
        selection = int(
            input(
                f"\n -----------------\n Which operation would you like to perform \n (PC={pc_on})? \n 01. PC on. \n 02. PC off. \n 03. Force shutdown \n 04. Restart \n 05. Clear CMOS \n 00. Return to start. \n \n >> "
            ))
        if selection == 1:
            if pc_on == "ON":
                print(bcolors.FAIL + "Pc is already on" + bcolors.ENDC)
                continue
            print(bcolors.OKGREEN + "PC turned ON!" + bcolors.ENDC)
            data["PC_STATUS"] = "OFF"
            with open("oc.json", "w+") as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
            pc_on = "on"
            continue
        elif selection == 2:
            if pc_on == "off":
                print(bcolors.FAIL + "PC is already turned off" + bcolors.ENDC)
                continue
            print(bcolors.WARNING + "PC turned OFF!" + bcolors.ENDC)
            data["PC_STATUS"] = "OFF"
            with open("oc.json", "w+") as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
            continue
        elif selection == 3:
            print("Forcing shutdown...")
            for x in range(3):
                print(".")
                print("..")
                print("...")
                time.sleep(0.1)
            pc_on = "off"
            print("Success")
            continue
        elif selection == 4:
            print("pc off")
            time.sleep(0.5)
            print("pc on")
            pc_on = "pc on"
            time.sleep(0.5)
            print("success")
            pc_on = "on"
            continue

        elif selection == 5:
            print("Clearing CMOS...")
            print("PC shutdown")
            pc_on = "off"
            continue
        elif selection == 00:
            break
        else:
            print("Invalid option")
            continue
