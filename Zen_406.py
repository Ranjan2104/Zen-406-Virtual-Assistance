import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import time
import smtplib
import wolframalpha
try:
    app = wolframalpha.Client("X27662-QTV98PXR56")
except Exception:
    print("NO found")

# Project Personal Assistance Zen 406;

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir! I Am Your Personal Assistent zen 406, How May I Help you")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir! I Am Your Personal Assistent zen 406, How May I Help you!")
    else:
        speak("Good Evening Sir! I Am Your Personal Assistent zen 406, How May I Help you!")


def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Hear you!......")
        audio = r.listen(source)
    try:
        print("Recognising Your Query Please Wait Sir......")
        text = r.recognize_google(audio, language='en-in')
        print(text)
    except Exception:
        speak("Sorry, Not Getting Your Voice!")
        print("Network Problem, Ask Again")
        return "none"
    return text


# for main function
if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()

        if "open wikipedia" in query or "please open wiki" in query or "please open wikipedia" \
                in query:
            speak("Searching Details Please Wait Sir......")
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            print(results)
            speak(results)
            webbrowser.open("www.wikipedia.com")
            speak("Opening Wikipedia Sir Please Wait")
        elif 'open youtube' in query or "please open youtube" in query or "play song on youtube" \
                in query or "play vedio on YouTube" in query:
            webbrowser.open("www.youtube.com")
            speak("Opening YouTube Sir Please Wait")
        elif 'open github' in query or "please open github" in query or "open my github account"\
                in query:
            webbrowser.open("https://www.github.com")
            speak("Opening Github Sir Please Wait")
        elif 'open facebook' in query or "please open facebook" in query or "open my facebook account"\
                in query:
            webbrowser.open("https://www.facebook.com")
            speak("Opening Facebook Sir Please Wait")
        elif 'open instagram' in query or "please open instagram" in query or "open my instagram" \
                in query:
            webbrowser.open("https://www.instagram.com")
            speak("Opening Instagram Sir Please Wait")
        elif 'open google' in query or "please open google" in query or "ok google" in query or \
                "hey google" in query or "search on google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google Sir Please Wait")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")

        elif 'open amazon' in query or 'please open amazon' in query or 'amazon' in query:
            webbrowser.open("https://www.amazon.in/")
            speak("Opening Amazon Sir Please Wait")

        elif 'open notepad++' in query:
            ll = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            speak("opening notepad++ please wait sir")
            os.startfile(ll)


        elif "close notepad" in query:
            speak("closing web browser")
            os.system('taskkill /f /im notepad.exe')

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")

        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com")
            speak("opening snapdeal")

        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")
        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")
        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")
        elif 'music from pc' in query or "music" in query:
            speak("ok i am playing music")
            music_dir = './music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, musics[0]))
        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = './video'
            videos = os.listdir(music_dir)
            os.startfile(os.path.join(video_dir, videos[0]))
        elif 'good bye' in query:
            speak("good bye")
            exit()
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')

        elif 'email to anyone' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! I am not able to send this email")

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy',
                      'i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            ans_take_from_user_how_are_you = takecom()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')
        elif 'who make you' in query or 'who created you' in query or 'who develop you' in query:
            ans_m = " For your information Amresh Mallick Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Zen 406 an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
        elif "hello" in query or "hey Zen" in query:
            hel = "Hello Amresh Sir ! How May i Help you.."
            print(hel)
            speak(hel)
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Zen"
            print(na_me)
            speak(na_me)
        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")
        elif query == 'none':
            continue
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query:
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()
        elif 'time please' in query or 'what is the time' in query or 'time batao' in query\
                or 'current time' in query or 'time' in query or 'whats time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(strTime)

        elif 'wait' in query or 'wait zen' in query or 'wait for second' in query or 'just wait' \
                in query or 'wait please' in query or 'please wait' in query or 'please wait zen'\
                in query or 'wait a second' in query:
            print("Ok! waiting sir")
            speak("OK! waiting sir")
            time.sleep(10)
            speak("OK sir! How May I Help You")
            print("OK sir! How May I Help You")

        elif 'temperature' in query:
            try:
                res = app.query(query)
                speak("Temperature is")
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("try again")

        elif 'plus' in query or '+' in query or 'add' in query:
            try:
                res = app.query(query)
                speak("Answer is")
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("Sorry! Speak again")

        elif 'substract' in query or '-' in query:
            try:
                res = app.query(query)
                speak("Answer is")
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("Sorry! Speak again")

        elif 'multiply' in query or 'x' in query:
            try:
                res = app.query(query)
                speak("Answer is")
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("Sorry! Speak again")

        else:
            temp = query.replace(' ', '+')
            g_url = "https://www.google.com/search?q="
            res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url + temp)

