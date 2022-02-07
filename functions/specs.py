import time, datetime, json, psutil, GPUtil, platform
from tabulate import tabulate
from functions.loop import loop
from misc_functions import bcolors

with open("specs.json", "r") as fp:
  data = json.load(fp)

def get_size(bytes, suffix="B"):
  factor = 1024
  for unit in ["", "K", "M", "G", "T", "P"]:
    if bytes < factor:
      return f"{bytes:.2f}{unit}{suffix}"
      bytes /= factor
options = [""]
def specs():
  for option in options:
    selection = int(input(f"\n -----------------\n Which component? \n 01. CPU \n 02. RAM \n 03. Disk \n 04. Network \n 05. GPU \n \n 06. Summary \n 00. Return to start. \n \n >> "))

    def get_size(bytes, suffix="B"):
      factor = 1024
      for unit in ["", "K", "M", "G", "T", "P"]:
          if bytes < factor:
              return f"{bytes:.2f}{unit}{suffix}"
          bytes /= factor




    if selection == 1: #cpu
      print(f"Computer network name: {platform.node()}")
      print(f"Machine type: {platform.machine()}")
      print(f"Processor type: {platform.processor()}")
      print(f"Operating system: {platform.system()}")
      print("Physical cores:", psutil.cpu_count(logical=False))
      print("Total cores:", psutil.cpu_count(logical=True))
      cpufreq = psutil.cpu_freq()
      print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
      print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
      print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
      # CPU usage
      print("CPU Usage Per Core:")
      for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
          print(f"Core {i}: {percentage}%")
      print(f"Total CPU Usage: {psutil.cpu_percent()}%")
      
    
    elif selection == 2: #ram
      print("="*40, "Memory Information", "="*40)
      # get the memory details
      svmem = psutil.virtual_memory()
      print(f"Total: {get_size(svmem.total)}")
      print(f"Available: {get_size(svmem.available)}")
      print(f"Used: {get_size(svmem.used)}")
      print(f"Percentage: {svmem.percent}%")
      print("="*20, "SWAP", "="*20)
      # get the swap memory details (if exists)
      swap = psutil.swap_memory()
      print(f"Total: {get_size(swap.total)}")
      print(f"Free: {get_size(swap.free)}")
      print(f"Used: {get_size(swap.used)}")
      print(f"Percentage: {swap.percent}%")
    
    elif selection == 3: #disk
      print("="*40, "Disk Information", "="*40)
      print("Partitions and Usage:")
      # get all disk partitions
      partitions = psutil.disk_partitions()
      for partition in partitions:
          print(f"=== Device: {partition.device} ===")
          print(f"  Mountpoint: {partition.mountpoint}")
          print(f"  File system type: {partition.fstype}")
          try:
              partition_usage = psutil.disk_usage(partition.mountpoint)
          except PermissionError:
              continue
          print(f"  Total Size: {get_size(partition_usage.total)}")
          print(f"  Used: {get_size(partition_usage.used)}")
          print(f"  Free: {get_size(partition_usage.free)}")
          print(f"  Percentage: {partition_usage.percent}%")
      disk_io = psutil.disk_io_counters()
      print(f"Total read: {get_size(disk_io.read_bytes)}")
      print(f"Total write: {get_size(disk_io.write_bytes)}")

    elif selection == 4: #network
      print("="*40, "Network Information", "="*40)
      if_addrs = psutil.net_if_addrs()
      for interface_name, interface_addresses in if_addrs.items():
          for address in interface_addresses:
              print(f"=== Interface: {interface_name} ===")
              if str(address.family) == 'AddressFamily.AF_INET':
                  print(f"  IP Address: {address.address}")
                  print(f"  Netmask: {address.netmask}")
                  print(f"  Broadcast IP: {address.broadcast}")
              elif str(address.family) == 'AddressFamily.AF_PACKET':
                  print(f"  MAC Address: {address.address}")
                  print(f"  Netmask: {address.netmask}")
                  print(f"  Broadcast MAC: {address.broadcast}")
      # get IO statistics since boot
      net_io = psutil.net_io_counters()
      print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
      print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

    elif selection == 5: #gpu
      print("="*40, "GPU Details", "="*40)
      gpus = GPUtil.getGPUs()
      list_gpus = []
      for gpu in gpus:
          gpu_id = gpu.id
          gpu_name = gpu.name
          gpu_load = f"{gpu.load*100}%"
          gpu_free_memory = f"{gpu.memoryFree}MB"
          gpu_used_memory = f"{gpu.memoryUsed}MB"
          gpu_total_memory = f"{gpu.memoryTotal}MB"
          gpu_temperature = f"{gpu.temperature} °C"
          gpu_uuid = gpu.uuid
          list_gpus.append((
              gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
              gpu_total_memory, gpu_temperature, gpu_uuid
          ))

      print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                        "temperature", "uuid")))






    elif selection == 6:
        physcores = psutil.cpu_count(logical=False)
        logicores = psutil.cpu_count(logical=True)
        cpusage = psutil.cpu_percent()
        cpufreq = psutil.cpu_freq()
        freq = (f"{cpufreq.current:.2f}Mhz")
        svmem = psutil.virtual_memory()
        totalmem = get_size(svmem.total)
        avamem = get_size(svmem.available)
        usemem = get_size(svmem.used)
        memusage = (f"{svmem.percent}%")


        print(f"CPU: \n >Cores: {physcores}\n >Threads: {logicores}\n >Load: {cpusage}\n >Clock: {freq}\n")
        print(f"RAM: \n >Used: {usemem}\n >Total: {totalmem}\n >Usage: {memusage}")
        print(f"Disk:")
      #print(psutil.sensors_temperatures())



    elif selection == 00:
      return