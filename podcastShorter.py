import sys
import videoProcessor
import audioProccesor
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os

if len(sys.argv) != 2:
    print("Usage python podcastShorter.py filename.mp4")
    sys.exit(1)

file = sys.argv[1]

####AUDIO####
audioProccesor.saveAudio(file)
audio = AudioFileClip("output.wav")
audioProccesor.transcriptAudio()


####VIDEO####
videoProcessor.saveVideo(file)
video = VideoFileClip("output.avi")



final = video.set_audio(audio)
final.write_videofile("short.mp4")


os.remove("output.avi")
os.remove("output.wav")