# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []




#------------------------------------------------------------------------------------------------------
#weather modules OpenWeather
#Account: ruven.peterhans@stud.kswe.ch password: Y8jYLzHZYqbE8Th
# API Key: bfafaca964b064d947e7a5f32faef634

#https://pypi.org/project/pyowm/
from typing import Any, Text, Dict, List
import os
import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from datetime import date, timedelta
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


 class Getweather(Action):

     def name(self) -> Text:
         return "action_get_weather"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         def getweather(location, day):
            if day=='today':
              d = date.today()
              print(d)
              owm1 = OWM('bfafaca964b064d947e7a5f32faef634')
              owm2= owm1.weather_manager()

              observation = owm2.weather_at_place(location+ ',' + 'CH')
              w = observation.weather
              k = w.detailed_status
              x = w.temperature('celsius')
              text='Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (location, k, x['temp_max'], x['temp_min'])

         dispatcher.utter_message(text)

         return []


def getweather(location, day):
  if day=='today':
    d = date.today()
    print(d)
    owm1 = OWM('bfafaca964b064d947e7a5f32faef634')
    owm2= owm1.weather_manager()

    observation = owm2.weather_at_place(location+ ',' + 'CH')
    w = observation.weather
    k = w.detailed_status
    x = w.temperature('celsius')
    print('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (location, k, x['temp_max'], x['temp_min']))

  if day == 'tomorrow':
    d= date.today() + timedelta(days=1)
    print(d)


    owm1 = OWM('bfafaca964b064d947e7a5f32faef634')
    owm2= owm1.weather_manager()

    observation = owm2.three_hours_forecast(location+ ',' + 'ch', limit=8)#only weather in switzerland
    w = observation.weather
    k = w.detailed_status
    x = w.temperature('celsius')
    print('The weather tomorrow in %s is %s. The maximum temperature will be %0.2f and the minimum temperature will be %0.2f degree celcius' % (location, k, x['temp_max'], x['temp_min']))

getweather('Genf','today')
getweather('Genf','tomorrow')
#------------------------------------------------------------------------------------------------------------

# set timer

# import the time module
import time
  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Fire in the hole!!')
   
# function call
#countdown(int(15)) #in seconds

#--------------------------------------------------------------------------------------------------------------

#translator 
from python_translator import Translator
def translator(content, language2, language1):
  translator = Translator()
  result = translator.translate(content,language2, language1)

  print(result)


#------------------------------------------------------------------------------------------------------------

#dictator
def dictate(text):
  with open("C:/Users/ruven/Desktop/dictation.txt", 'w') as f:
    f.write(text)




#-------------------------------------------------------------------------------------

#create appointment
#password google account school:
#ruven.peterhans@stud.kswe.ch
#4rQwAV7fq9nNQXS




# Imagine this function is part of a class which provides the necessary config data
import win32com.client
from win32com.client import Dispatch
outlook = win32com.client.Dispatch("Outlook.Application")


def createEvent():
  appt = outlook.CreateItem(1) # AppointmentItem
  appt.Start = "2022-9-12 16:10" # yyyy-MM-dd hh:mm
  appt.Subject = "Fake meeting"
  appt.Duration = 30 # In minutes (60 Minutes)
  appt.Location = "The bat cave"

  appt.Save()
  appt.Send()

