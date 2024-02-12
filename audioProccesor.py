from moviepy.editor import VideoFileClip
import speech_recognition as sr

def saveAudio(file):
    clip = VideoFileClip(file)
    audio = clip.audio
    audio.write_audiofile("output.wav")
    clip.close()
    
def transcriptAudioWithTimestamps(audio_file):
    recognizer = sr.Recognizer()

    # Load audio file
    audio = sr.AudioFile(audio_file)
    
    with audio as source:
        audio_data = recognizer.record(source)
        
    try:
        # Recognize audio with timestamps
        result = recognizer.recognize_google(audio_data, show_all=True, language="pl-PL")
        
        # Extract text and timestamps from the result
        subtitles = []
        for alternative in result['alternative']:
            text = alternative['transcript']
            
            # Check if 'timestamps' key exists
            if 'timestamps' in alternative:
                for word, start_time, end_time in alternative['timestamps']:
                    subtitles.append((start_time, end_time, word))
            else:
                # Handle missing timestamps
                print("No timestamps found for alternative:", text)
        
        return subtitles
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
