
#voice command testing code


# Python program to translate
# speech to text and text to speech


import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import cv2
import pytesseract# will convert the image to text string
import gtts  
from playsound import playsound 
from PIL import Image
from googletrans import Translator
from pygame import mixer
from gtts import gTTS #Import Google Text to Speech
from IPython.display import Audio #Import Audio method from IPython's Display Class



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning buddy!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon buddy!")  

    else:
        speak("Good Evening!")  

    speak("I am Jarvis. how may I help you!")      

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please...!!!!")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'Hi' in query:
            speak('Hi buddy')
            
        elif 'take photo' in query:
            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            while(result):
                ret,frame = videoCaptureObject.read()
                cv2.imwrite("C:/Users/shang/TechOcular/imagetaken1.jpg",frame)
                result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            if True :
                
                    img = Image.open("C:/Users/shang/TechOcular/imagetaken1.jpg")
                

                   # describes image format in the output
                    print(img)
                   # path where the tesseract module is installed
                    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
                   #This .exe is attached in my repositary
                   # converts the image to result and saves it into result variable
                    result = pytesseract.image_to_string(img)
                   # write text in a text file and save it to source path
                    with open('C:/Users/shang/TechOcular/imagetaken1.txt',mode ='w') as file:

                       file.write(result)
    
                    file = open("C:/Users/shang/TechOcular/imagetaken1.txt", "r")
                    a=file.read()
        
                    tts = gTTS(str(a)) #Provide the string to convert to speech
                    tts.save('C:/Users/shang/TechOcular/imagetaken1.mp3') #save the string converted to speech as a .wav file
                    sound_file = 'C:/Users/shang/TechOcular/imagetaken1.mp3'
                    Audio(sound_file, autoplay=True)
      
                    translator = Translator()
                    result= translator.translate(result, dest="en")
                    print(result)
                 
                             
            elif 'play audio' in query:
                          mixer.init()

                          # Loading the song
                          mixer.music.load("C:/Users/shang/TechOcular/imagetaken1.mp3")

                          # Setting the volume
                          mixer.music.set_volume(0.9)

                          # Start playing the song
                          mixer.music.play()

                          # infinite loop
                        
                          while True:
                              if 'pause' in query:
                                  mixer.music.pause()	
                              elif 'resume' in query:
                                  mixer.music.unpause()
                              elif 'stop' in query:
                                      # Stop the mixer
                              	mixer.music.stop()
                              	break

               	
            elif 'pause audio' in query:
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
                                
       




                                

                        
                        
                   
      
