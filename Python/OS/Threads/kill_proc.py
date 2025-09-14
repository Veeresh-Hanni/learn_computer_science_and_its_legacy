import subprocess, time, psutil

# 1. Open Notepad
subprocess.Popen(["notepad.exe"])
print("✅ Notepad opened.")

# 2. Wait 5 seconds
time.sleep(5)

# 3. Kill ALL Notepad processes
for proc in psutil.process_iter(['pid', 'name']):
    try:
        if proc.info['name'] and proc.info['name'].lower() == "notepad.exe":
            print(f"❌ Closing Notepad with PID: {proc.info['pid']}")
            proc.kill()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

print("✅ All Notepad processes have been closed.")
