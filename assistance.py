import speech_recognition as sr
import  time
import webbrowser
from gtts import  gTTS
import playsound
import os
import wikipedia

r=sr.Recognizer()

def recognize_speech(ask=False):
    with sr.Microphone() as source: 
        if ask:
            speak(ask)
        audio=r.listen(source)
        print("Processing...")
        audio_data=''
        try:
            audio_data=r.recognize_google(audio)
            print(audio_data)
        except sr.UnknownValueError:
            speak("Sorry, I could not understand. can you say again?")
            # audio_data = recognize_speech()
        except sr.RequestError as e:
            speak("Sorry, the service is not available")
        return audio_data
        
def response(audio_data):
    if audio_data  == 'what is your name':
        speak("my name is shisir")

    if audio_data == 'what time is it now':
        t=time.localtime()
        speak(time.strftime("%H:%M:%S", t))


    if 'search' in audio_data:
        search=recognize_speech('what do you want to search?')
        url='https://www.google.com/search?q='+search
        speak('here is the result for you')
        webbrowser.open(url)
        # print('search')

    if 'location' in audio_data:
        location=recognize_speech('what is your location')
        url='https://google.nl/maps/place/' + location + '/&amp;'
        speak('here is your location')
        webbrowser.open(url)

    if audio_data == 'Wikipedia':
        search=recognize_speech('what do you want to search for in wikipedia?')
        # print(search)
        try:
            wiki_data=wikipedia.summary(search,sentences=3)
            print(wiki_data)
            time.sleep(3)
            speak(wiki_data)
        except wikipedia.exceptions.DisambiguationError as e:
            speak('Sorry, i couldnot understand')


    if 'exit' in audio_data or 'quit' in audio_data:
        speak('Good bye. have a nice day')
        exit()

def speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    fileName="voice.mp3"
    tts.save(fileName)
    playsound.playsound(fileName)
    os.remove(fileName)
    print(audio_string)
        
# delay to prevent code from immediately exiting
time.sleep(1)

# loop until exit
speak("How can i help you?")
while 1:
    audio_data=recognize_speech()
    # print(audio_data)
    response(audio_data)


        