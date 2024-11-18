import platform
import psutil
import datetime
import time
import os

def get_size(bytes):
  """
  Convert bytes to correct size (KB, MB, GB, TB..)
  """

  for size in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
    # As long as bytes > 1024 means we haven't found the correct size
    # When size < 1024, means the correct size is found.    
    if bytes < 1024:
      return f"{bytes:.2f}{size}"
    bytes /= 1024

def get_system_info():
  """
  Get general OS, Uptime, Average Load Info
  """
  print('-' * 100)
  print(f"=== System Performance Report ===")
  print(f"TimeStamp: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
  print('-' * 100)
  
  # os details
  print(f"=== OS Details ===")
  print(f"OS Detailed: {platform.platform()}")
  print(f"OS Name: {platform.system()}")
  print(f"OS Architecture: {platform.architecture()}")
  print(f"System UpTime: {datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%d-%m-%Y %H:%M:%S')}")
  print(f"Python Version: {platform.python_version()}")
  # Check if the system is Unix-like before calling os.getloadavg()
  if os.name == 'posix':
      print(f"System Average Load: {os.getloadavg()}")
  else:
      print("System Average Load: Not available on this OS")
  print('-' * 100)

def get_cpu_info():
  print(f"=== CPU Info ===")
  print(f"How many physical cores?: {psutil.cpu_count(logical=False)}")
  print(f"Total Cpu Usage?: {psutil.cpu_percent(interval=1, percpu=False)}%")
  print('-' * 100)

def get_memory_info():
  print(f"=== Memory Info ===")
  memory = psutil.virtual_memory()
  print(f"Total RAM In Machine?: {get_size(memory.total)}")
  print(f"RAM in use: {get_size(memory.used)}")
  print(f"RAM used in %: {memory.percent}%")
  print(f"RAM available: {get_size(memory.available)}")
  print('-' * 100)

def get_disk_info():
    print(f"=== Storage/Disk Usage ===")
    disk = psutil.disk_usage('/')
    print(f"Total Disk In Machine?: {get_size(disk.total)}")
    print(f"Disk used: {get_size(disk.used)}")
    print(f"Disk used in %: {disk.percent}%")
    print(f"Disk available: {get_size(disk.free)}")
    print('-' * 100)

def get_top_processes():
    print("=== Top 5 CPU-Consuming Processes ===")
    processes = []
    
    # First iteration to start CPU monitoring
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Call cpu_percent() once to initialize CPU monitoring
            proc.cpu_percent()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    """
    Wait for a second to get meaningful CPU values
    
    If we call proc.cpu_percent() two times and put a gap of some second between these two calls
    by using time.sleep() then for that gap the cpu_usage_percentage will be given.
    
    Othwerwise cpu_usage_percentage will always be shown 0 as no time/gap was given
    to gather the cpu_usage. Because cpu usage is calculated over time/sec, so this 
    time.sleep() is needed.
    """
    time.sleep(1)
    
    # Second iteration to get actual CPU values
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            cpu_percent = proc.cpu_percent()
            processes.append({
                'pid': proc.pid,
                'name': proc.name(),
                'cpu_percent': cpu_percent
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    # Sort by CPU usage
    """
    **This single line of code below can be confusing..
    So here is a little explanation:
    
      Processes list contains 'process dict object' kind of similar to json/dictionary to eyes.
      Sort the processes list in descending order (reverse=True).
      Use lambda function to set the key.
      List will be sorted on the basis of the 'cpu_percent' of each object in the list.
      As list is sorted in descending order on the basis of 'cpu_percent' we can get
      top 5 using [:5] slicing syntax.
    
    **Lambda Functions:
      A lambda function in Python is a small anonymous function defined with the lambda keyword. 
      It can have any number of arguments, but only one expression. 
      The expression is evaluated and returned. 
      Lambda functions are often used for short, throwaway functions that are not complex enough 
      to warrant a full function definition.
      
    **Lambda Syntax:
      lambda arguments: expression
    """
    top_cpu = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:5]
    for proc in top_cpu:
        print(f"PID: {proc['pid']:<10} Name: {proc['name']:<20} CPU: {proc['cpu_percent']:.1f}%")
    print('-' * 100)

    # --- Get Top 5 Memory Using Processes ---
    print("=== Top 5 Memory-Consuming Processes ===")
    
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
      try:
        processes.append(proc.info)
      except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
    
    top_memory_processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:5]
    for proc in top_memory_processes:
      print(f"PID: {proc['pid']:<10} Name: {proc['name']:<20} Mem_Usage: {proc.get('memory_percent', 0):.2f}%")
    print('-' * 100)
    
def get_loggedIn_users():
    print(f"=== Currently LoggedIn Users ===")
    users = psutil.users()
    for user in users:
        # Get attributes with default values if they don't exist
        """
        The reason for using `or 'N/A` in `getattr(user, 'name', 'N/A') or 'N/A'`
        is that `getattr` will give 'N/A' as output only if `user.<attribute name>`
        key is not present at all.
        
        But there is a edge case. What if `user.<attribute name>` is present but its
        values is `None`. This outputs errors if value is `None` for print() statement.
        
        So `or N/A` is a another safety net used here, to make sure we get `N/A` even if
        the `user.<attribute name>` is `None`.
        
        For example:
        1. Let's say `name = getattr(user, 'name', 'N/A')` outputs None.
        2. Now we have `None or 'N/A'. None is falsy. 'N/A' string is truthy.
        3. 'N/A' is chosen as its truthy.
        """
        name = getattr(user, 'name', 'N/A') or 'N/A'  # Use 'N/A' if name is None
        terminal = getattr(user, 'terminal', 'N/A') or 'N/A'  # Use 'N/A' if terminal is None
        host = getattr(user, 'host', 'N/A') or 'N/A'  # Use 'N/A' if host is None
        
        # Format the string with the guaranteed non-None values
        print(f"User: {str(name):<10} User's Terminal: {str(terminal):<10} User's Host: {str(host)}")
    print('-' * 100)

def main():
  get_system_info()
  get_cpu_info()
  get_memory_info()
  get_disk_info()
  get_top_processes()
  get_loggedIn_users()

if __name__ == "__main__":
  main()
