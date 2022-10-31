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
       
        location = next(tracker.get_latest_entity_values("location"), None)
        day = next(tracker.get_latest_entity_values("date"), None)
#        dispatcher.utter_message(location)
#        dispatcher.utter_message(day)
        
        if day=='today':
          owm1 = OWM('bfafaca964b064d947e7a5f32faef634')
          owm2= owm1.weather_manager()

          observation = owm2.weather_at_place(location + ',' + 'CH')
          w = observation.weather
          k = w.detailed_status
          x = w.temperature('celsius')
          text='Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (location, k, x['temp_max'], x['temp_min'])

        dispatcher.utter_message(text)
        
        return []

#------------------------------------------------------------------------------------------------------------

# set timer
# time needs to be given in minutes
# import the time module
import time
import datetime



# define the countdown func.
class Settimer(Action):

     def name(self) -> Text:
        return "action_get_timer"
        

     def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       

        t = next(tracker.get_latest_entity_values("timelength"), None)

#        dispatcher.utter_message(t)

        def countdown(h, m, s):
 
          # Calculate the total number of seconds
          total_seconds = h * 3600 + m * 60 + s
       
          # While loop that checks if total_seconds reaches zero
          # If not zero, decrement total time by one second
          while total_seconds > 0:
       
              # Timer represents time left on countdown
              timer = datetime.timedelta(seconds = total_seconds)
              
              # Prints the time left on the timer
              print(timer, end="\r")
       
              # Delays the program one second
              time.sleep(1)
       
              # Reduces total time by one second
              total_seconds -= 1
       
          print("Bzzzt! The countdown is at zero seconds!")

        countdown(0,int(t),0)
        
          
        dispatcher.utter_message("timer is set")

        return[]
        
   


#--------------------------------------------------------------------------------------------------------------

#translator 
from python_translator import Translator

class Translation(Action):

     def name(self) -> Text:
        return "action_get_translation"
        

     def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        transinput = next(tracker.get_latest_entity_values("transinput"), None)
        language = next(tracker.get_latest_entity_values("language"), None)
#        dispatcher.utter_message(transinput)
#        dispatcher.utter_message(language)
 
        translator = Translator()
        transoutput = translator.translate(transinput, language, "english")
        transoutput=str(transoutput)
        spell=str()
        for i in transoutput:
          spell+= str(" " + i)

        text=(transinput + " in " + language + " means " + transoutput + ". This is written" + spell )
        dispatcher.utter_message(text)
        return[]


#------------------------------------------------------------------------------------------------------------

#dictator
class Dictator(Action):

     def name(self) -> Text:
        return "action_get_dictation"
        

     def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       

        dictation = next(tracker.get_latest_entity_values("dictation"), None)
#        dispatcher.utter_message(dictation)
        
        with open("C:/Users/ruven/Desktop/dictation.txt", 'w') as f:
          f.write(dictation)

        dispatcher.utter_message(text="dictation saved")
        return[]




#-------------------------------------------------------------------------------------
#
#create appointment
#only full hours like 12 o'clock

import win32com.client
from win32com.client import Dispatch
outlook = win32com.client.Dispatch("Outlook.Application")


class Appointmentcreator(Action):

     def name(self) -> Text:
        return "action_get_appointment"
        

     def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       

        time = next(tracker.get_latest_entity_values("time"), None)
        day = next(tracker.get_latest_entity_values("date"), None)
        title = next(tracker.get_latest_entity_values("title"), None)
        
        # '10 o'clock' am to '10:00'
        t = [int(i) for i in time.split() if i.isdigit()]
        t= int(t[0])
        if "pm" in time:
          t=t+12
          if t == 24:
            t=0
        if t < 10:
          t = str(t)
          t = " 0" + t
        elif t <=10:
          t=str(t)
          t = " " + t
        t=str(t)
        t = t + ":00"

        # 10th november to 2022-11-10
        d = [str(i) for i in day if i.isdigit()]
        if len(d) == 1:
          d.insert(0, "0")
        d = ''.join(d)

        if "january" in day:
          m="01"
        if "february" in day:
          m="02"
        if "march" in day:
          m="03"
        if "april" in day:
          m="04"
        if "june" in day:
          m="05"
        if "july" in day:
          m="06"
        if "" in day:
          m="07"
        if "august" in day:
          m="08"
        if "september" in day:
          m="09"
        if "october" in day:
          m="10"
        if "november" in day:
          m="11"
        if "december" in day:
          m="12"

        result=str("2022-" + m + "-" + d + t)
#        dispatcher.utter_message(result)
        
        appt = outlook.CreateItem(1) # AppointmentItem
        appt.Start = result # yyyy-MM-dd hh:mm
        appt.Subject = title
        appt.Duration = 60 # In minutes

        appt.Save()
        appt.Send()

        dispatcher.utter_message(text="An appointment was created in your calendar ")
        
        return[]

