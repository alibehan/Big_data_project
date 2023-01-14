
# Real Time Big Data Project

## accessing of real time weather data from Openweather API

## API Reference

#### Creat an account at openWeather API and then login to you account 
#### There you will see a row of with some attributes like new products, services, API keys, click at API keys, you will see generate key option click at generate key and give name to key then you will see following informition there

```http   
```
| KEY | name      | status               |
| :-------- | :------- | :------------------------- |
| api_key | respective name | Active |

### libraries Required 
 ##### - Request 
 ##### - Kafka-python
 ##### - pyspark  

### Install docker desktop https://www.docker.com/products/docker-desktop/

#### Create docker compose yml file in you project folder. In docker yml file put the configuration of containers and brocker.the respective configuration of containers is available in docker compose yml file in respository.you can see from there.

## producer.py 
#### this file  read the data from open Weather api and the write to the kafka 
### file is there in respository
## if you want to write code by yourself  for reading and writing to kafka.
### write code in the language which you prefer.In this project case the python is used. 
#### It is better to create an schema of respective parameters of data like Temperature, humidity and so on. but if you want to explore whole streaming dataset, In that Case the create an schema is not important.

### write of straming data 
#### since we are writing straming data to kafka so we need to create a topic and send the data to kafka with respective topic.
### KAFKA UI  
#### open kafka  UI with respective localhost port (http://localhost:28080)
### kafka_spark_stream.py 
#### In  this file we read the data from Kafka and possibly change it in tabualr or structural form.Since in this project the psotgresql is used.so, possible setup of postgresql is required to do that create a sql file with a table in it created with respective column attributes and their datatype properties.then there is effort to connect postgresql with spark streamed data. 

###  pgAdmin 
#### open pgadmin localhost with respective port(http://localhost:20080) and to connect with server fill the required configuration information like port number, localhost address, database name, user and passward.all these configuration informition should be exaclty same what it is available in docker compose ylm file.
### Graphana 
#### localhost. http://localhost:23000
#### For dashboarding of data in Graphana you need to connect graphana to posgres database.Provide the configuration information to connect graphana to postgres database. To keep the datasource remin connected, Skipping  yourself from connecting datasource again and again at every attempt of running the graphana localhost.So, there is need to create a child folder inside graphana folder  with all.yml file.Further, configuration details of file is available in respository with all.yml file. Likewise, to keep your dashboard and respective panels remain there in graphana, when attempting to coonect graphana localhost again and again.So, there is need to create folder name dashboard inside the graphana folder.inside the dashboard folder create dashboard.json file and put the json of your dashboard and to keep your dashboard there create all.yml file inside the dashboard folder .the configuration information of the all.yml file is there is respository  


