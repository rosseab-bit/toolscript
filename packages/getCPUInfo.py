# -*- coding: utf-8 -*-
import os
import sys
import json
import psutil
import time
def getCPUInfo():
    print ('='*40, 'CPU Info', '='*40)
    # NUCLEOS
    print ('Physical cores:', psutil.cpu_count(logical=False))
    print ('Total cores:', psutil.cpu_count(logical=True))
    # FRECUENCIA
    cpufreq = psutil.cpu_freq()
    print (f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print (f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print (f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # USO DEL CPU
    print ('CPU Usage Per Core:')
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        print (f"Core {i}: {percentage}%")
    print (f"Total CPU Usage: {psutil.cpu_percent()}%")
getCPUInfo()
