#https://realpython.com/python-speech-recognition/
import speech_recognition as sr
"""recognize_bing(): Microsoft Bing Speech
recognize_google(): Google Web Speech API
recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
recognize_houndify(): Houndify by SoundHound
recognize_ibm(): IBM Speech to Text
recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
recognize_wit(): Wit.ai"""

cur_dir = r"D:\Phansa2\Speech\data\audio_files"

r = sr.Recognizer()

#without background noise
audio_file = cur_dir+ r"\harvard.wav"
harvard = sr.AudioFile(audio_file)
with harvard as source:
    audio = r.record(source)

type(audio)
r.recognize_google(audio)



#with background noise
jackhammer = sr.AudioFile(cur_dir+  r'\jackhammer.wav')
with jackhammer as source:
    r.adjust_for_ambient_noise(source, duration=.2) #if can't pick up words adjust duration to be slower when default is 1
    audio2 = r.record(source)

r.recognize_google(audio2)
r.recognize_google(audio2, show_all=True)


#Microphone class if we want to use live input
mic = sr.Microphone()
sr.Microphone.list_microphone_names()
mic = sr.Microphone(device_index=3) #pick which mic u wanna use

with mic as source:
    r.adjust_for_ambient_noise(source)
    myspeech = r.listen(source) #listens until silence is detected 

r.recognize_google(myspeech) 
