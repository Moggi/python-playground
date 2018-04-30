import subprocess
import time

p = subprocess.Popen(["python3", "busy_process.py", "argzZZ"])
print(p.pid)

print(vars(p))
# print(p.args)
# print(p.args[2])

p.wait()
