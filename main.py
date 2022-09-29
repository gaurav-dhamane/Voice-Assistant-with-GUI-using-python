from tkinter import Entry, Tk,StringVar,Label,PhotoImage,Button  #gui
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

root = Tk()  # Tkinter object

# All dir:
# Change Folder address
music_dir = "" 
chrome_path = "C:\\Users\\Dell\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
codePath = 'C:\\Program Files\\Microsoft VS Code\\Code.exe'
py_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe"
pp = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT'
word = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD'
c_path = 'C:\\Users\\Dell\\Desktop\\Apps\\control'
i_path = 'C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.2.2\\bin\\idea64.exe'

# URL:
g_url = "https://www.google.com/search?q="
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # you can try different voices by changing the number inside square brackets

global var
global var1
var = StringVar()
var1 = StringVar()

def update(ind):
    frame = MI[ind % 51]
    ind += 1
    label.configure(image=frame)
    root.after(50, update, ind)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def start():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        var.set("Good Morning!")
        root.update()
        speak("Good Morning!")
    elif 12 <= hour <= 18:
        var.set("Good Afternoon!")
        root.update()
        speak("Good Afternoon !")
    else:
        var.set("Good Evening!")
        root.update()
        speak("Good Evening !")


def take_command():
    global query

    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening..")
        root.update()
        r.pause_threshold = 0.6
        r.energy_threshold = 600
        audio = r.listen(source)

    try:
        var.set("Recognizing..")
        root.update()
        query = r.recognize_google(audio, language='en-in')
        root.update()

    except Exception :
        speak('Say that again')
        take_command()

    var1.set(query)
    root.update()
    return query


def play():
    start()
    speak("How may I help you?")
    while True:
        # global query
        query = take_command()
        query = query.lower()
        try:
            
            if 'stop listening' in query:
                var.set("")
                root.update()
                speak("Sure sir!")
                break

            elif 'wikipedia' in query:
                speak('Searching wikipedia..')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences= 2)
                speak("According to Wikipedia")
                var.set(query)
                root.update()
                speak(results)

            elif 'news' in query:
                speak("Here's the letest news")
                webbrowser.get('chrome').open_new_tab('https://www.ndtv.com/')
                break

            elif 'open youtube' in query:

                var.set('opening Youtube')
                root.update()
                speak('opening Youtube')
                webbrowser.get('chrome').open_new_tab('youtube.com')

            elif 'open google' in query:
                var.set('opening google')
                root.update()
                speak('opening google')
                webbrowser.get('chrome').open_new_tab('google.com')

            elif 'hello' in query:
                var.set('Hello Sir')
                root.update()
                speak("Hello Sir")

            elif 'play music' in query:
                songs = os.listdir(music_dir)
                n = random.randint(0, 32)
                os.startfile(os.path.join(music_dir, songs[n]))
              

            elif 'the time' in query:
                str_time = datetime.datetime.now().strftime("%I:%M %p")
                var.set(f"Sir, the time is {str_time}")
                root.update()
                speak(f"Sir, the time is {str_time}")

            elif 'the date' in query:
                str_date = datetime.datetime.today().strftime("%d %m %y")
                var.set("Sir today's date is %s" % str_date)
                root.update()
                speak("Sir today's date is %s" % str_date)

            elif 'thank you' in query:
                var.set("Welcome Sir")
                root.update()
                speak("Welcome Sir")

            elif 'open pycharm' in query:
                var.set("Opening Pycharm")
                root.update()
                speak("Opening Pycharm")
                os.startfile(py_path)

                break

            elif 'open intellij idea' in query:
                var.set("opening intellij idea")
                root.update()
                os.startfile(i_path)
                speak('opening intelliJ IDEA')

                break

            elif 'open PowerPoint' in query:
                var.set("opening powerpoint")
                root.update()
                os.startfile(pp)
                speak('Opening Microsoft PowerPoint')

                break

            elif 'open Word' in query:
                var.set("opening word")
                root.update()
                os.startfile(word)
                speak('Opening Microsoft Word')

                break

            elif 'open chrome' in query:
                var.set("Opening Google Chrome")
                root.update()
                speak("Opening Google Chrome")
                os.startfile(chrome_path)

                break

            elif 'open control panel' in query:
                var.set("opening control panel")
                root.update()
                os.startfile(c_path)
                speak('Opening control Panel')


            elif 'none' in query:
                continue
            elif 'exit' in query:
                root.destroy()

            elif "shutdown" in query:
                speak("Do you want to switch off the computer sir?")
                query = take_command()
                query = query.lower()
                if "yes" in query:
                    speak("Shutting Down the Computer")
                    os.system("shutdown /s /t 1")

                else:
                    continue

            else:
                var.set("Searching for " + query)
                root.update()
                speak('Searching for ' + query)
                webbrowser.get('chrome').open_new_tab(g_url + query)

        except Exception:
            speak("I didn't Understand")
            
# GUI

label2 = Label(root, textvariable=var1, bg='black',  fg='cyan')
label2.config(font=("Open Sans", 20))

var1.set('')
label2.grid(row=0, column=0)


label1 = Label(root, textvariable=var, bg='black', fg='cyan')
label1.config(font=("Open Sans", 20))
var.set('Welcome')
label1.grid(row=1, column=0)

MI = [PhotoImage( file='final.gif',
                 format=f'gif -index {i}')for i in range(51)]
root['bg'] = 'black'
root.title("ELSA")
root.iconbitmap(r'app_icon.ico')

label = Label(root, bg='black', width=400, height=500)
label.grid()

root.after(0, update, 0)

# Buttons
btn1 = Button(text='PLAY', width=20, command=play, bg='black', fg='cyan')
btn1.config(font=("Open Sans", 12))
btn1.grid()
btn2 = Button(text='EXIT', width=20, command=root.destroy, bg='black', fg='cyan')
btn2.config(font=("Open Sans", 12))
btn2.grid()
root.mainloop()
