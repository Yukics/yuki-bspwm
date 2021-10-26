#!/bin/python3
import os

free=int((os.popen("cat /proc/meminfo | head -3 | tail -1 | awk '{print $2}'").read().strip("\n")))
total=int((os.popen("cat /proc/meminfo | head -1 | awk '{print $2}'").read().strip("\n")))
res="MEM:"+"{:.2f}".format((total-free)*100/total)+"%"

print(res)