import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime

#khoitao
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    #nghe
    today = date.today()
    now = datetime.now()


    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening !!")
        audio = robot_ear.listen(mic)
        print("Robot : ...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
        
    #trituenhantao
    print("You :" + you)
    if you == "":
        robot_brain = "I can't hear you, try again !!"
    elif "hello" in you:
        robot_brain = "Hello Mr Duy"
    elif "today" in you:
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        robot_brain = now.strftime("%H:%M:%S")
    elif "president" in you:
        robot_brain = "Donald Trump"
    elif "bye" in you:
        robot_brain = "I'm fine thanks you !!"
        print("Robot : " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "Thanks"
        
        
    print("Robot : " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()