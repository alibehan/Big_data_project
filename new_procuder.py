import time
import datetime
import json
from kafka import KafkaProducer
import requests





kafka_topic = 'sampletopic1'

producer = KafkaProducer(bootstrap_servers='localhost:29092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'), api_version=(0, 10, 1))

jason_message = None
city_name = None
temperature = None
humidity = None
weather_api_endpoint = None
applied = None


def weather_detail(weather_api_endpoint):
    api_response = requests.get(weather_api_endpoint)
    jason_data = api_response.json()
    #print(jason_data)
    city_name = jason_data['name']
    humidity = jason_data['main']['humidity']
    temperature = jason_data['main']['temp']
    feel_like=jason_data['main']['feels_like']
    temp_diff=jason_data['main']['feels_like']-jason_data['main']['temp_max']
    tempmin=jason_data['main']['temp_min']
    tempmax=jason_data['main']['temp_max']
    wind_speed=jason_data['wind']['speed']
    Country= jason_data['sys']['country']
    jason_message = {'country':Country,'city_name': city_name, 'temperature': round(temperature),'temp_min':round(tempmin),'temp_max':round(tempmax),'feel_like':round(feel_like),'humidity': humidity,
                   'wind_speed':round(wind_speed ),'temp_diff':round(temp_diff), 'creation_time': datetime.datetime.now().isoformat()}
    return jason_message


def main(appied):

    while True:
        for city_name in ['Quetta','Islamabad','Karachi','Murree','Peshawar ']:
            appied ='APIKEY'

            weather_api_endpoint = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid={appied}'

            jason_message = weather_detail(weather_api_endpoint)
            print(jason_message)
            producer.send(kafka_topic,jason_message)

            print('wait for 10 seconds')
            time.sleep(2)
            producer.flush()





if __name__ == '__main__':
   main(producer)


