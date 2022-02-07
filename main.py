import time, datetime, json, threading, sys, os
from functions.pcsettings import pcoperation
from functions.logging import logging
from functions.temps import temps
from functions.specs import specs
from functions.loop import loop

functions = {
    '1': specs,
    '2': pcoperation
    '3': temps,
    '4': logging
}


def main():
    n = 1
    availablefns = [
        "Specs", "PC Settings", "Temps", "Start Logging"
    ]
    print("Select a function (number):  ")
    for x in range(len(availablefns)):
        print(f"{n}. {availablefns[x]}")
        n += 1

    fns = [""]
    for fn in fns:
        a = str(input("\n>> "))
        try:
            functions[a]()
        except KeyError:
            print("Function not found.")
            time.sleep(3)
            clearConsole()
            main()


try:
    main()
    
except Exception as e:
    print(e)
