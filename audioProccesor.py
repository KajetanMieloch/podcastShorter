from moviepy.editor import VideoFileClip
import speech_recognition as sr

def saveAudio(file):
    clip = VideoFileClip(file)
    audio = clip.audio
    audio.write_audiofile("output.wav")
    clip.close()
    
def transcriptAudio():
    recognizer = sr.Recognizer()
    audio = sr.AudioFile("output.wav")
    
    with audio as source:
        audio = recognizer.record(source)
        
    try:
        text = recognizer.recognize_google(audio, language="pl-PL")
        print("Text:", text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))