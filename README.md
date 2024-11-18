# server-performance-stats
A cross-platform `machine performance stats` script project written in python3. Tested on windows and ubuntu linux.

## How to run this project on your machine ?
#### 1. Install python on your laptop/pc above 3.10+
  Go to internet and install python for your machine.

#### 2. Make sure these python libraries are installed on your pc/laptop.
  ```python
  import platform
  import psutil
  import datetime
  import time
  import os

  # Use 'pip' to install these if you dont have these.
  ```
#### 3. Clone the repository
  In your terminal execute: git clone https://github.com/navraj-singh-dev/server-performance-stats.git<br>
  Otherwise just download the code as zip.

#### 4. Run the server_stats.py file
  Run this file on vscode or your terminal (recommended).<br>
  Your terminal will output the output of this script.<br>
  Done!<br>

#### 5. Sample output of this script
  ```plaintext
  ----------------------------------------------------------------------------------------------------
  === System Performance Report ===
  TimeStamp: 18-11-2024 15:36:30
  ----------------------------------------------------------------------------------------------------
  === OS Details ===
  OS Detailed: Windows-10-10.0.22631-SP0
  OS Name: Windows
  OS Architecture: ('64bit', 'WindowsPE')
  System UpTime: 14-11-2024 15:42:07
  Python Version: 3.10.6
  System Average Load: Not available on this OS
  ----------------------------------------------------------------------------------------------------
  === CPU Info ===
  How many physical cores?: 4
  Total Cpu Usage?: 20.0%
  ----------------------------------------------------------------------------------------------------
  === Memory Info ===
  Total RAM In Machine?: 23.84GB
  RAM in use: 10.80GB
  RAM used in %: 45.3%
  RAM available: 13.04GB
  ----------------------------------------------------------------------------------------------------
  === Storage/Disk Usage ===
  Total Disk In Machine?: 475.83GB
  Disk used: 211.56GB
  Disk used in %: 44.5%
  Disk available: 264.26GB
  ----------------------------------------------------------------------------------------------------
  === Top 5 CPU-Consuming Processes ===
  PID: 0          Name: System Idle Process  CPU: 64.9%
  PID: 12740      Name: UninstallMonitor.exe CPU: 65.2%
  PID: 15128      Name: python.exe           CPU: 35.1%
  PID: 16948      Name: os_server.exe        CPU: 19.1%
  PID: 10288      Name: Code.exe             CPU: 2.7%
  ----------------------------------------------------------------------------------------------------
  === Top 5 Memory-Consuming Processes ===
  PID: 3156       Name: MemCompression       Mem_Usage: 4.94%
  PID: 16948      Name: os_server.exe        Mem_Usage: 4.39%
  PID: 7728       Name: chrome.exe           Mem_Usage: 1.71%
  PID: 7236       Name: Code.exe             Mem_Usage: 1.66%
  PID: 9436       Name: TextInputHost.exe    Mem_Usage: 1.52%
  ----------------------------------------------------------------------------------------------------
  === Currently LoggedIn Users ===
  User: name       User's Terminal: N/A        User's Host: N/A
  ----------------------------------------------------------------------------------------------------
  ```

## Want to read my blog on this project ?
  Here is my linkedin article/blog on this project..<br>
  [My LinkedIn Article On This Project](https://www.linkedin.com/pulse/building-server-performance-monitoring-tool-devops-project-singh-qynoc/?trackingId=NieaDXvERMqN1mySbLx6PA%3D%3D)
