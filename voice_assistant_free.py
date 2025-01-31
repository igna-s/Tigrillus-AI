#pip install pipwin
#pipwin install pyaudio
#pip install pyttsx3



"""
Commands in English and Spanish:
Start YouTube / Abrir YouTube

English: "Start YouTube"
Spanish: "Abrir YouTube"

Start Google / Abrir Google
English: "Start Google"
Spanish: "Abrir Google"

What day it is / ¿Qué día es?
English: "What day it is"
Spanish: "¿Qué día es?"

What time it is / ¿Qué hora es?
English: "What time it is"
Spanish: "¿Qué hora es?"

Goodbye / Adiós
English: "Goodbye"
Spanish: "Adiós"

Search on Wikipedia / Buscar en Wikipedia
English: "Wikipedia" (followed by the search term)
Spanish: "Wikipedia" (seguido de la búsqueda)

Your name / Tu nombre
English: "What's your name?"
Spanish: "¿Cuál es tu nombre?"

Search for something / Buscar en internet
English: "Search for" (followed by the search term)
Spanish: "Busca en internet" (seguido de la búsqueda)

Song / Reproducir canción
English: "Song" (followed by the song name)
Spanish: "Canción" (seguido del nombre de la canción)

Joke / Contar un chiste
English: "Joke"
Spanish: "Chiste"

Stock price / Valor de la bolsa
English: "Stock price" (followed by the company name, e.g., 'apple', 'tesla', etc.)
Spanish: "Valor bolsa" (seguido del nombre de la empresa, por ejemplo: 'apple', 'tesla', etc.)

Saludo // Say hello
English: "hi, my name is" (followed by the name)
Spanish: "hola, mi nombre es" (seguido del nombre)

"""
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



# Transform speech to text

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





# give the day
def the_day(idioma):
    day = datetime.date.today()
    weekday = day.weekday()  # Cambiado a método
    #print(weekday)
   
    if idioma:
        mapping = {
           0: "Lunes",
           1: "Martes",
           2: "Miércoles",
           3: "Jueves",
           4: "Viernes",
           5: "Sábado",
           6: "Domingo"
        }
        try:
            speaking(f'Hoy es {mapping[weekday]}', idioma)  # Añadido el argumento 'idioma' a speaking
        except Exception as e:
            print(f"Error: {e}")
    
    if not idioma:
        mapping = {
           0: "Monday",
           1: "Tuesday",
           2: "Wednesday",
           3: "Thursday",
           4: "Friday",
           5: "Saturday",
           6: "Sunday"
        }

        try:
            speaking(f'Today is {mapping[weekday]}', idioma)  # Añadido el argumento 'idioma' a speaking
        except Exception as e:
            print(f"Error: {e}")



#give the time
def the_time(idioma):
    time = datetime.datetime.now().strftime("%I:%M")  
    print(time)
    
    if idioma:

        try:
            speaking(f'La hora actual es {time[0:2].lstrip("0")} y {time[3:5].lstrip("0")}', idioma)  
        except Exception as e:
             print(f"Error: {e}")
    
    if not idioma:
        try:
            speaking(f'The current time is {time[0:2].lstrip("0")} o` clock and {time[3:5].lstrip("0")} minutes', idioma)  
        except Exception as e:
            print(f"Error: {e}")

#Introduction
def whatsup(idioma):
    if not idioma: speaking("Hi, my name is Tigrillus. I am your personal assistant. How can I help you today?", False)
    else: speaking("¿Qué tal? Mi nombre es Tigrillus. Soy tu asistente personal. ¿En qué puedo ayudarte hoy?", True)


#Assistant "Brain"

def assistant(idioma):
    start = True
    whatsup(idioma)
    
    while start and not idioma:
        aux = transform(idioma).lower()

        if "start youtube"  in aux:
             speaking("Opening Youtube", idioma)
             webbrowser.open("https://www.youtube.com/")
             continue
        elif "start google" in aux:
             speaking("Opening Google", idioma)
             webbrowser.open("https://www.google.com/")
             continue
        elif "what day it is" in aux:
             the_day(idioma)
             continue
        elif "what time it is" in aux:
             the_time(idioma)
             continue
        elif "goodbye" in aux:
             start = False
             speaking("Goodbye", idioma)
       
       
        elif "wikipedia" in aux:
             speaking("Searching in Wikipedia...", idioma)
             aux = search = aux.split("wikipedia")[-1].strip()
             wikipedia.set_lang("en")  # Configura el idioma de Wikipedia a español
             try:
                 result = wikipedia.summary(aux, sentences=2)  # Obtiene un resumen con 2 oraciones
                 speaking(f"Acording to Wikipedia: {result}", idioma)
             except wikipedia.exceptions.DisambiguationError as e:
                 speaking(f"Ambiguous search, Please try again: {', '.join(e.options[:5])}", idioma)
             except wikipedia.exceptions.PageError:
                 speaking(f"Article related to {aux} has not been found.", idioma)
             except Exception as e:
                 speaking(f"Error: {e}", idioma)
             continue

        elif "your name" in aux:
             speaking("My name is Tigrillus, I am your assistant", idioma)
             continue
        elif "search for" in aux:
             pywhatkit.search(aux)
             speaking("Esto es lo que encontré", idioma)
             continue
        elif "song" in aux:
             song = aux.replace("song", "")
             speaking("Now youre listening to " + song, idioma)
             pywhatkit.playonyt(song)
             continue
        elif "joke" in aux:
             speaking(pyjokes.get_joke(language="en"), idioma)   
             continue
        elif "stock price" in aux:
             search = aux.split("price")[-1].strip().lower()
             lookup = { 'apple': 'AAPL', 'amazon': 'AMZN', 'google': 'GOOGL','microsoft': 'MSFT','facebook': 'FB', 'tesla': 'TSLA','bitcoin': 'BTC-USD'
        }
             try:
                 stock = lookup[search]
                 stock_data = yf.Ticker(stock)
                 current_price = stock_data.history(period='1d')['Close'][-1]
                 current_price = round(current_price, 2)
                 speaking(f'The current price of {search} is {current_price}', idioma)
             except:
                 speaking(f'Sorry, I cannot find the stock price for {search}', idioma)
                 continue
        elif "name is" in aux:
             search = aux.split("is")[-1].strip()
             speaking(f'Nice to meet you {search}', idioma)
             speaking("My name is Tigrillus, I am your assistant, what can i do for you", idioma)
             continue


        time.sleep(2)
        
    while start and idioma:
         aux = transform(idioma).lower()
         if "abrir youtube" in aux:
             speaking("Abriendo YouTube", idioma)
             webbrowser.open("https://www.youtube.com/")
             continue
         elif "abrir google" in aux:
             speaking("Abriendo Google", idioma)
             webbrowser.open("https://www.google.com/")
             continue
         elif "qué día es" in aux:
             the_day(idioma)
             continue
         elif "qué hora es" in aux:
             the_time(idioma)
             continue
         elif "adiós" in aux:
             start = False
             speaking("Adiós", idioma)
         
         elif "wikipedia" in aux:
             speaking("Buscando en Wikipedia...", idioma)
             aux = search = aux.split("wikipedia")[-1].strip()
             wikipedia.set_lang("es")  # Configura el idioma de Wikipedia a español
             try:
                 result = wikipedia.summary(aux, sentences=2)  # Obtiene un resumen con 2 oraciones
                 speaking(f"De acuerdo a Wikipedia: {result}", idioma)
             except wikipedia.exceptions.DisambiguationError as e:
                 speaking(f"Tu búsqueda es ambigua. Por favor, especifica más: {', '.join(e.options[:5])}", idioma)
             except wikipedia.exceptions.PageError:
                 speaking(f"No se encontró un artículo en Wikipedia relacionado con {aux}.", idioma)
             except Exception as e:
                 speaking(f"Lo siento, ocurrió un error al buscar en Wikipedia. Error: {e}", idioma)
             continue



         elif "tu nombre" in aux:
             speaking("Mi nombre es Tigrillus, Soy tu asistente personal", idioma)
             continue
         elif "busca en internet" in aux:
             song = aux.replace("busca en internet", "")
             pywhatkit.search(aux)
             speaking("Esto es lo que encontré", idioma)
             continue
         elif "canción" in aux:
             song = aux.replace("cancion", "")
             speaking("Ahora estas escuchando " + song, idioma)
             pywhatkit.playonyt(song)
             continue
         elif "chiste" in aux:
             speaking(pyjokes.get_joke(language="es"), idioma)   
             continue
         elif "valor bolsa" in aux:
             search = aux.split("bolsa")[-1].strip().lower()
             lookup = {'apple': 'AAPL', 'amazon': 'AMZN', 'google': 'GOOGL', 'microsoft': 'MSFT', 'facebook': 'FB', 'tesla': 'TSLA', 'bitcoin': 'BTC-USD'}
             try:
                 stock = lookup[search]
                 stock = yf.Ticker(stock)
                 current_price = stock.history(period='1d')['Close'][-1]
                 current_price = round(current_price, 2)
                 speaking(f'El precio actual de {search} es {current_price}', idioma)
             except:
                 speaking(f'Lo siento, no puedo encontrar el precio de {search}', idioma)
             continue
         elif "nombre es" in aux:
             search = aux.split("es")[-1].strip()
             speaking(f'Encantado de conocerte {search}', idioma)
             speaking("Mi nombre es Tigrillus, Soy tu asistente personal, que puedo hacer por ti?", idioma)
             continue
         time.sleep(2)
       
    
#Main
idioma = True #True is Spanish
assistant(idioma)