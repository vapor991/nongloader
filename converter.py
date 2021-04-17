#this is a very small script i know
import os.path as path
import moviepy.editor as mp 

def extract_audio(source: str):
    video = mp.VideoFileClip(source)
    target = path.splitext(source)[0] + '.mp3'
    video.audio.write_audiofile(target, bitrate='320k', write_logfile=False) #u can change this bitrate if u want but dont count on it working
    video.close()