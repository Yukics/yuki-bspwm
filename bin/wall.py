#!/bin/python3

import time
import sys
import os
from PIL import Image

on = os.system('ps -aux | grep "wall.py" | wc -l')

if on > 0:
    os.system('killall wall.py')

file = sys.argv[1]

if file == "":
    print("Dame un parametro plox, un gif")

if not file.endswith(".gif"):
    print("Introduce un gif")

if os.path.isdir('/tmp/wall'):
    os.system('rm -r /tmp/wall && mkdir /tmp/wall')
else:
    os.system('mkdir /tmp/wall')

num_key_frames = int(os.popen("identify "+file+"| wc -l").read())

with Image.open(file) as im:
    for i in range(num_key_frames):
        im.seek(im.n_frames // num_key_frames * i)
        im.save('/tmp/wall/{}.png'.format(i))

times = os.popen("identify "+file+" | cut -d ':' -f 2").read().split("s")
timing = [s.replace("\n", "") for s in times]
while("" in timing) :
    timing.remove("")

while True:
    
    for pic in zip(range(num_key_frames), timing):
        print(pic)
        os.system('feh --bg-fill /tmp/wall/'+str(pic[0])+'.png')
        time.sleep(float(pic[1])*10)
    pic=[]