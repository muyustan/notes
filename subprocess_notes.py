#! /usr/bin/env python3
# import sys
# import subprocess
# import os
# import datetime

"""

mod_time = os.stat('document').st_mtime
print(datetime.datetime.fromtimestamp(mod_time))

"""
"""
 if len(sys.argv) > 1:
     print(sys.argv[1])
 else:
     print("Not enough arguments!!!")

 bash scripting $1 $2 etc.

 subprocess.run("ls -l ~", shell=True)
 if shell=True is not used, then you have to give the arguments as a list
 of strings for example; subprocess.run(["ls", "-l"])

 s = subprocess.check_output("ls -l ~", shell=True)
 print(s.decode()) # utf-8 argument is not mandatory
 s is originally a byte object.
 this is the way you make it to recognize '\n' character.

 an alternative to all these: (not on python3.6 but on python3.7)
 s = subprocess.run('ls -l', shell=True, text=True, capture_output=True)
 print(s.stdout)
"""
