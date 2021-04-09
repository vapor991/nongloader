import gd
import os
import shutil
import time
from os import walk

locations = open('locations.txt', 'r')
locations = locations.readlines()
source = locations[2]
source = source.split('|')
source = source[1]
source = source.strip()
destination = locations[3]
destination = destination.split('|')
destination = destination[1]
destination = destination.strip()
memory = gd.memory.get_memory()
_, _, filenames = next(walk(source))

do_print = True
songid = 0

if memory.is_in_level():
    if do_print:
        songid = str(memory.get_song_id())
        print(songid)
    do_print = False
else:
    do_print = True
    print('A level is not open! Please open a level in gd.')

for char in filenames:
    extension = char[-3:]
    if extension == 'mp3':
        songname = char
    else:
        continue

print(songname)
songidfile = f'{songid}.mp3'
os.rename(songname, songidfile)
source = source + songidfile
destination = destination + songidfile
if os.path.exists(source) == False:
    print('Error with locations.txt!')
if os.path.exists(destination) == True:
    os.remove(destination)
dest = shutil.move(source, destination)
time.sleep(1)
print('Song loaded!')
