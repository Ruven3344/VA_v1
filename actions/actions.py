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
#weather modules https://pypi.org/project/python-weather/
import python_weather
import asyncio
import os

async def getweather():
  # declare the client. format defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(format=python_weather.IMPERIAL) as client:

    # fetch a weather forecast from a city
    weather = await client.get("location") #location
  
    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)
  
    # get the weather forecast for a few days
    for forecast in weather.forecasts:
      print(forecast.date, forecast.astronomy)
  
      # hourly forecasts
      for hourly in forecast.hourly:
        print(f' --> {hourly!r}')

if __name__ == "__main__":
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(getweather())
#------------------------------------------------------------------------------------------------------------

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
      
    print('Timer ended')
  
  
# input time in seconds
t = timelength
  
# function call
countdown(int(t))

#--------------------------------------------------------------------------------------------------------------

#translator modules
from python_translator import Translator

translator = Translator()
result = translator.translate(transinput, "english", language)

print(result)

#------------------------------------------------------------------------------------------------------------

