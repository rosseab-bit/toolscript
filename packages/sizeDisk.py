# -*- coding: utf-8 -*- 
import os
import sys
import psutil
import json

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def sizeDisk():
    print ('='*40, 'Disk information', '='*40)
    print ('Partitions and Usage:')
    partitions = psutil.disk_partitions()
    print (partitions)
    for partition in partitions:
        print (f"=== Device: {partition.device} ===")
        print (f"   Mountpoint: {partition.mountpoint}")
        print (f"   File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print (f"   Total Size: {get_size(partition_usage.total)}")
        print (f"   Used: {get_size(partition_usage.used)}")
        print (f"   Free: {get_size(partition_usage.free)}")
        print (f"   Percentage: {get_size(partition_usage.percent)}")
sizeDisk()
