import gd
import os
import shutil
import time
import urllib.request
import re
from os import walk
from pytube import YouTube
from converter import extract_audio
#i cant remember if i need all these but im pretty sure i do

source = __file__.replace('nongloader.py', '')
start = 'c:\\Users\\'
end = '\\'
user = ((__file__.split(start))[1].split(end)[0])
destination = f'c:\\users\\{user}\\appdata\\local\\geometrydash\\'

memory = gd.memory.get_memory()
_, _, filenames = next(walk(source))
songname = False
conv = False
do_print = True
#booleans! :D
songid = 0

if memory.is_in_level():
    if do_print:
        songid = str(memory.get_song_id())
        print(songid)
    do_print = False
else:
    do_print = True
    print('A level is not open! Please open a level in gd.')
    time.sleep(3)
    exit()

for char in filenames:
    extension = char[-3:]
    if extension == 'mp3':
        songname = char
    else:
        continue

if songname == False:
    conv = True
    keyword = input('Search for song via youtube:')
    if keyword.startswith('https:'):
        video_url = keyword
    else:
        keyword = keyword.replace(' ', '+')
        html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + keyword)
        video_ids = re.findall(r'watch\?v=(\S{11})', html.read().decode())
        video_url = 'https://www.youtube.com/watch?v=' + video_ids[0]
    yt=YouTube(video_url)
    t=yt.streams.all()
    t[0].download(source)
    _, _, filenames = next(walk(source))
    for char in filenames:
        extension = char[-3:]
        if extension == 'mp4':
            songname = char
        else:
            continue
    extract_audio(songname)
    songname = songname[:-3] + 'mp3'

#genuinely have no idea what i did to make this work

print(songname)
songidfile = f'{songid}.mp3'    
os.rename(songname, songidfile)
if conv == True:
    delmp4 = songname[:-3] + 'mp4'
    os.remove(delmp4)
    print('song downloaded and converted!')

source = source + songidfile
destination = destination + songidfile
print(f'destination exists: {os.path.exists(destination)}.')
print(f'source exists: {os.path.exists(source)}.')
print(source)
print(destination)

if os.path.exists(source) == False:
    print('Error with locations.txt!')

if os.path.exists(destination) == True:
    print('song already exists! deleting file...')
    os.remove(destination)

dest = shutil.move(source, destination)
print('Song loaded!')
time.sleep(3)