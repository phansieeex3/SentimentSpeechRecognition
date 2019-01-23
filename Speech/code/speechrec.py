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


#Python libraries used, libraries not installed can be installed using "pip install <libraryname>"
#Microsoft API website to try sample emails: https://azure.microsoft.com/en-us/services/cognitive-services/text-analytics/
import urllib
import json
from http.client import HTTPSConnection
import requests
#Made a Text Analytics Service of Azure

#Our Base URL:
uri = "westcentralus.api.cognitive.microsoft.com"
#Our Access Key:
accessKey = '4f1cf05ba8d545f2bdb137168d66c8f0'

def GetSentiment (documents):
    #Path to the Sentiment Analysis Microsoft API:
    path = "/text/analytics/v2.0/sentiment" #sentiment HTTP/1.1
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

#Json format required by the API:
documents = { 'documents': [
    { 'id': '1', 'language': 'en', 'text': 'Hi team, So today I looked at your analysis the data seems to be working properly but I wish it was better. I would like a meeting of this sooner later this week. Let’s catch up and taco-about it' },
    { 'id': '2', 'language': 'en', 'text': 'I demand a report' }
]}

#Saving results generated in a Json:
result = GetSentiment(documents)
print("Resulting scores for each Document:", result)
#Saving json:
sentiments = json.loads(result)["documents"]
