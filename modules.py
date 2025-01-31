import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os
import yfinance as yf
import pyjokes
import time
import wikipedia



# Transform speech to text, true is spanish and false is english

import speech_recognition as sr

def transform(idioma):
    r = sr.Recognizer()

    if not idioma:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=None, phrase_time_limit=None)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-US')  # US English
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Say that again please...")
            return "I am waiting for your command"
        except sr.RequestError:
            print("I am not available now")
            return "I am waiting for your command"
        except:
            return "I am waiting for your command"
        return query
    else:
        with sr.Microphone() as source:
            print("Escuchando...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=None, phrase_time_limit=None)
        try:
            print("Reconociendo...")
            query = r.recognize_google(audio, language='es-AR')  # Español de Argentina
            print(f"Lo que dijiste es: {query}\n")
        except sr.UnknownValueError:
            print("No entendí, por favor repite...")
            return "Estoy esperando =D"
        except sr.RequestError:
            print("No estoy disponible ahora")
            return "Estoy esperando =D"
        except:
            return "Estoy esperando =D"
        return query


# Speaking function (from text to speech)
def speaking(message,idioma):
    engine = pyttsx3.init()


    # Filter the message to include only letters, numbers, and spaces
    message = ''.join(char for char in message if char.isalnum() or char.isspace())

    # Show all available voices in your computer, If you want another just install it
    #for voice in engine.getProperty('voices'):
    #    print(voice, voice.id)
    #id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"   #spanish (Mexico)
     
    if idioma: id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"  #Spanish (Spain)
    else: id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"   #English (United States)
    
    engine.setProperty('voice', id)
    engine.setProperty('rate', 150)  # Speed
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
    engine.say(message)
    engine.runAndWait()



