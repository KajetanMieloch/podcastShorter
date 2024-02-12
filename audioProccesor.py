from moviepy.editor import VideoFileClip


def saveAudio(file):
    clip = VideoFileClip(file)
    audio = clip.audio
    audio.write_audiofile("output.wav")
    clip.close()