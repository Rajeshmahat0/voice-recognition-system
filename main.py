import speech_recognition as sr
import webbrowser                # we can open any browser
import pyttsx3                   # It converts text to speech
import musicLibrary
import requests                   # requests to get the data inside the link


#pip install pocketsphinx

recognizer = sr.Recognizer()    # It recognizes the speech
engine = pyttsx3.init()          #initailize pyttsx3
newsapi = "a5476781753b4ffd9c82095da3924875"



def speak(text):    #speak function
    engine.say(text)      #this will say the text             
    engine.runAndWait()  #after saying the text it will wait



# def aiProcess(commnd):
#     client = OpenAI(api_Key = "<Your Key Here >"
#     )


def processCommand(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://youtube")
    elif "open linkedin" in c.lower():
        speak("opening linkedin")
        webbrowser.open("https://linkedin")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]    #.split converts to list["play", "skyfall"]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():          #37 to 49 for getting news headlines...
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=a{newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
           data = r.json()
    
           # Extract the list of articles
           articles = data.get('articles', [])
    
           # Extract and print the headlines
           for article in articles:
            headline = article.get('title')
            print(headline)
    else:
        #Let openAI handle the requests
        pass

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "Listening"):  ########################
                speak("Yesss")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))




