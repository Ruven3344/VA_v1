# import the time module
import time
import pyttsx3
time=t[0]
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.setProperty("rate", 100)
    engine.say(command)
    engine.runAndWait()

# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    #SpeakText("The timer is over")
SpeakText(time)
  
  
# input time in seconds

# function call
#countdown(int(t))

