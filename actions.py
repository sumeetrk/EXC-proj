from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests

class ActionWeather(Action):
    def name(self):
        return 'action_weather'
    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = '6b920954bbadcac7f4d473d13e8079a4' #your apixu key
        client = ApixuClient(api_key)
        loc = tracker.get_slot('location')
        result=requests.get('http://api.weatherstack.com/current',{'access_key': api_key,'query': str(loc)})
        current=result.json()
        print(current)
        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['weather_descriptions']
        temperature_c = current['current']['temperature']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_speed']
        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]