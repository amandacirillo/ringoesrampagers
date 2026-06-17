import subprocess, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

cwd = r'C:\temp\ringoesrampagers'

r1 = subprocess.run(['git', 'add', '-A'], capture_output=True, text=True, cwd=cwd)
print("add:", r1.stdout.strip() or "ok")

r2 = subprocess.run(['git', 'commit', '-m', 'Reorder sections, infinite looping carousel'], capture_output=True, text=True, cwd=cwd)
print("commit:", r2.stdout.strip())
if r2.stderr.strip(): print("commit err:", r2.stderr.strip())

r3 = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True, cwd=cwd)
print("push:", r3.stdout.strip() or r3.stderr.strip())
print("code:", r3.returncode)
