import pyttsx3
import datetime
from time import sleep
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate',130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()
r.energy_threshold = 300

def getTime():
    hour = int(datetime.datetime.now().hour)
    hour%=12
    minutes = int(datetime.datetime.now().minute)
    return str(hour)+":"+str(minutes)

def getDate():
    date = datetime.datetime.now()
    return str(date.day)+"-"+str(date.month)+"-"+str(date.year)
    
def Wish()->str:
    hour = int(datetime.datetime.now().hour)
    return ("Morning" if (hour>=9 and hour<=12) else "Afternoon")

def takeCommand():
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

class  AutomatedAttedence:
    presentResponse = ['present','present mam',"present ma'am"]
    absentResponse = ['absent','absent mam',"absent ma'am"]
    def __init__(self):
        self.presentList = []
        self.absentList = []
        engine.say("Please enter the Section")
        engine.runAndWait()
        self.section = input("Enter Your Section\n").upper()
        engine.say("Please enter the total strength of the class\n")
        engine.runAndWait()
        self.maxStudents = int(input("Enter total strength\n"))
        engine.say("Which Period is it?")
        engine.runAndWait()
        self.period = int(input("Enter Period\n"))
        engine.say("Which SUbject is currently running?")
        engine.runAndWait()
        self.subject = input("Enter Subject\n").upper()
        with open(f"{self.section} {getDate()}", "a") as f: 
            f.write(f"Date:-{getDate()}\n")

    def takeAttedence(self):
        engine.say("I will be taking your attendence now please be quite")
        sleep(1)
        # engine.say("I am a bit old and cannot hear properly so please speak loud")
        engine.runAndWait()
        for i in range(1,self.maxStudents+1):
            engine.say(f"Roll Number {i}")
            engine.runAndWait()
            ans = takeCommand()
            while ((ans not in AutomatedAttedence.presentResponse) and (ans not in AutomatedAttedence.absentResponse)):
                engine.say("Sorry I did not get You Can You Please Repeat again")
                ans = takeCommand()
                engine.runAndWait()
            if ans in AutomatedAttedence.presentResponse:
                self.presentList.append(i)
            if ans in AutomatedAttedence.absentResponse:
                self.absentList.append(i)

    def getPresentList(self):
        print("The Present Roll Numbers are : ",end=" ")
        for i in self.presentList:
            print(i,end = " ")
    
    def generateAttendenceSheet(self):
        with open(f"{self.section} {getDate()}", "a") as f: 
            f.write(f"Time : {getTime()}\n{self.period}.{self.subject}:- Present Roll Numbers are {self.presentList}  Absent Roll Numbers are {self.absentList}\n")

def sayPresentRollNumbers(sec):
        engine.say("The Present Roll Numbers are ")
        engine.runAndWait()
        for i in range(len(sec.presentList)):
            engine.say(sec.presentList[i])
            engine.runAndWait()

def sayAbsentRollNumbers(sec):
    engine.say("The Absent Roll Numbers are ")
    for i in range(len(sec.absentList)):
        engine.say(sec.absentList[i])
        engine.runAndWait()

CSM = AutomatedAttedence()
CSM.generateAttendenceSheet()
CSM.takeAttedence()
engine.say('I can read out the present or absent roll numbers')
engine.say('If You want to me to terminate the program say yes otherwise say no')
engine.runAndWait()
ans = takeCommand().lower()

while(ans not in 'yes terminate' and (ans not in 'no do not terminate')):
    engine.say('Sorry did not understand what you said please repeat again')
    engine.runAndWait()
    ans = takeCommand().lower()

if(ans=='no'):
    engine.say('To get present roll numbers say speakout present roll numbers')
    engine.say('To get absent roll numbers say speakout absent roll numbers')
    engine.runAndWait()
    cmd = takeCommand().lower()
    if("present roll numbers" in cmd):
        sayPresentRollNumbers(CSM)
    elif("absent roll numbers" in cmd):
        sayAbsentRollNumbers(CSM)