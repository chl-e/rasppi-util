import time, datetime, json, psutil, GPUtil, sys
from tabulate import tabulate

def temps():
    if not hasattr(psutil, "sensors_temperatures"):
        print("\n>Platform not supportd.   ")
        return
    temps = psutil.sensors_temperatures()
    if not temps:
        print("\n>Cannot read any temperatures.  ")
        return
    for name, entries in temps.items():
        print(name)
        for entry in entries:
            print("    %-20s %s °C (high = %s °C, critical = %s °C)" % (
                entry.label or name, entry.current, entry.high,
                entry.critical))
        print()