import sys
import subprocess
import os
import time
#import psutil

print('sys.argv[1]: ' + sys.argv[1])

for filename in os.listdir(sys.argv[1]):
    fullname = sys.argv[1] + filename
    subprocess.call(['java', '-jar', 'omnisia202101261131.jar', '-i', fullname, '-o', sys.argv[2], '-draw'])
    print("hello, yes its me, your python program. I'm still alive and kicking!")
    #time.sleep(2)

# subprocess.call(['java', '-jar', 'OMNISIA20160926.jar', '-i', sys.argv[1], '-o', sys.argv[2], '-draw', '-a', 'Forth', '&'])
# for proc in psutil.process_iter():
#     print(proc.name())
