import subprocess, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
cwd = r'C:\temp\ringoesrampagers'
r1 = subprocess.run(['git', 'add', '-A'], capture_output=True, text=True, cwd=cwd)
r2 = subprocess.run(['git', 'commit', '-m', 'Remove duplicate Races and Photos sections'], capture_output=True, text=True, cwd=cwd)
print("commit:", r2.stdout.strip())
r3 = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True, cwd=cwd)
print("push:", r3.stdout.strip() or r3.stderr.strip())
print("code:", r3.returncode)
