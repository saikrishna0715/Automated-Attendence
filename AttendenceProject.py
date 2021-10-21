import pyttsx3
import datetime
from time import sleep
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate',130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def Greet():
    engine.say(f"Good {Wish()} Students")
    sleep(1)
    engine.say("I will be taking your attendence now please be quite")
    sleep(1)
    engine.say("I am bit old and cannot hear properly so please speak loud")
    engine.runAndWait()

def getTime():
    hour = int(datetime.datetime.now().hour)
    minutes = int(datetime.datetime.now().minute)
    return str(hour)+":"+str(minutes)

def getDate():
    date = datetime.datetime.now()
    return str(date.day)+"-"+str(date.month)+"-"+str(date.year)
    
def Wish()->str:
    hour = int(datetime.datetime.now().hour)
    return ("Morning" if (hour>=9 and hour<=12) else "Afternoon")

def Wait():
    sleep

def takeCommand()->str:
    r = sr.Recognizer()
    # r.adjust_for_ambient_noise(source, duration=5)
    r.pause_threshold = 0.8
    r.energy_threshold = 250
    with sr.Microphone() as source:
        engine.say('I am Listening')
        engine.runAndWait()
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        return "None" 
    return query

class  AttedenceProject:
    presentResponse = ['present','present mam',"present ma'am"]
    absentResponse = ['absent','absent mam',"absent ma'am"]
    def __init__(self,maxStudents):
        self.presentList = []
        self.absentList = []
        self.maxStudents = maxStudents
        engine.say("Which Section is this ?")
        engine.runAndWait()
        self.section = input("Enter Your Section\n").upper()
        engine.say("Which Subject is Currently Running?")
        engine.runAndWait()
        self.period = input("Enter Subject\n").upper()

    def takeAttedence(self):
        for i in range(1,self.maxStudents+1):
            engine.say(f"Roll Number {i}")
            engine.runAndWait()
            ans = takeCommand()
            while ((ans not in AttedenceProject.presentResponse) and (ans not in AttedenceProject.absentResponse)):
                engine.say("Sorry I did not get You Can You Please Repeat again")
                ans = takeCommand()
                engine.runAndWait()
            if ans in AttedenceProject.presentResponse:
                self.presentList.append(i)
            if ans in AttedenceProject.absentResponse:
                self.absentList.append(i)

    def sayPresentRollNumbers(self):
        engine.say("The Present Roll Numbers are ")
        engine.runAndWait()
        sleep(1)
        for i in range(len(self.presentList)):
            engine.say(self.presentList[i])
            engine.runAndWait()
            sleep(1)

    def sayAbsentRollNumbers(self):
        engine.say("The Absent Roll Numbers are ")
        for i in range(len(self.absentList)):
            engine.say(self.absentList[i])
            engine.runAndWait()
    def getPresentList(self):
        print("The Present Roll Numbers are : ",end=" ")
        for i in self.presentList:
            print(i,end = " ")
    
    def attendenceSheet(self):
        with open(f"{self.section} {getDate()}", "a") as f: 
            f.write("Hello World!!!") 


CSM = AttedenceProject(5)

# while (getTime()!="4:10"):
#     print("Hello")

CSM.attendenceSheet()