import os
import sys
import codecs
import time
import subprocess

i=""                            # input srt name
subprocess.call("python know-word.py -n %s" % (str(i)), shell=True)
subprocess.call("python movieDubbed.py -n %s" % (str(i)), shell=True)
print("run success")
