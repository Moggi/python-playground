import subprocess
import time

p = subprocess.Popen(["python3","busy_process.py"])
print(p.pid)
