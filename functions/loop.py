import time, datetime, json, psutil, GPUtil, threading
from tabulate import tabulate
from datetime import datetime
now = datetime.now()

def loop():
    f = open(f"data/specs.txt", "r+")
    f.truncate(0)
    with open("oc.json", "r") as fp:
      data = json.load(fp)

    f.write("CPU USAGE: \n")
    for x in data["CPUCores Usage"]:
        f.write(f"{json.dumps(x)}\n")

    f.write("\nCPU FREQS: \n")
    for y in data["CPUCores Freq"]:
        f.write(f"{json.dumps(y)}\n")
    ram = data["RAM "]
    f.write(f"\nRAM: \n{ram}")
    f.close()
    time.sleep(1)
    f.close()
   

