
import json
import os
import sys
import psutil
import platform
def systemInfo():
    print ('='*40, 'System information', '='*40)
    uname = platform.uname()
    print (f"System: {uname.system}")
    print (f"Node Name: {uname.node}")
    print (f"Release: {uname.release}")
    print (f"Version: {uname.version}")
    print (f"Machine: {uname.machine}")
    print (f"Processor: {uname.processor}")

systemInfo()
