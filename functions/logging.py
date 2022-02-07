import time, datetime, json, psutil, GPUtil, threading
from functions.loop import loop
from tabulate import tabulate


def logging():
      def get_size(bytes, suffix="B"):
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor
      t = 30
      p = 0
      while p < t:
        physcores = psutil.cpu_count(logical=False)
        logicores = psutil.cpu_count(logical=True)
        cpusage = psutil.cpu_percent()
        cpufreq = psutil.cpu_freq().current
        freq = (f"{cpufreq:.2f}Mhz")
        svmem = psutil.virtual_memory()
        totalmem = get_size(svmem.total)
        avamem = get_size(svmem.available)
        usemem = get_size(svmem.used)
        memusage = (f"{svmem.percent}%")



        data = {}
        usage_list = [{f"Core {i}": percentage} for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1))]
        data['CPUCores Usage'] = usage_list

        freq_list = [{f"Core {i}": freq} for i, freq in enumerate(psutil.cpu_freq(percpu=True))]
        data['CPUCores Freq'] = freq_list
        data["PC_STATUS"]= "ON"

        ram = {"Used: ": usemem, "Total: ": totalmem, "Usage: ": memusage}
        data['RAM ']= ram

        with open('oc.json', 'w+') as fp:
            json.dump(data,fp, sort_keys=True, indent=4)

        #thread = threading.Thread(target=loop, args=(1,), daemon=True)
        loop()
        p += 1