import sys
import videoProcessor
import audioProccesor
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os

if len(sys.argv) != 2:
    print("Usage python podcastShorter.py filename.mp4")
    sys.exit(1)

file = sys.argv[1]

videoProcessor.saveVideo(file)
audioProccesor.saveAudio(file)

video = VideoFileClip("output.avi")
audio = AudioFileClip("output.wav")

final = video.set_audio(audio)
final.write_videofile("short.mp4")

os.remove("output.avi")
os.remove("output.wav")