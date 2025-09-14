# import psutil

# print("PID\tName\t\tStatus")
# for proc in psutil.process_iter(['pid', 'name', 'status']):
#     print(f"{proc.info['pid']}\t{proc.info['name']}\t{proc.info['status']}")

import subprocess, psutil, time

# Start a process (example: sleep for 10 seconds)
process = subprocess.Popen(["notepad.exe"])
print(f"Started process with PID: {process.pid}")

# Show process table and check if our process is listed
print("\nProcess Table (showing first 10):")
for proc in list(psutil.process_iter(['pid', 'name', 'status']))[:10]:
    print(proc.info)

# Wait 3 seconds, then terminate the process
time.sleep(3)
process.terminate()
process.kill()
print(f"Process with PID {process.pid} terminated.")
