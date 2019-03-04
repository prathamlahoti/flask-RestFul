# Flask RESTful API

## Prerequisite
This extremely simple application is intended to show, how easily we can create and manage web APIs,
using remote mongoDB cloud storage and docker containers. Don't pay attention on the code. It looks ugly, for sure. The purpose of this project is to play with technologies and get some more practice.


## About
The application represents a simple RESTful API using mongoDB and Docker. We're using [mongoDb.Atlas](https://cloud.mongodb.com) service for remote access to our mongoDB. You could check connection options to this service right there or on [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) documentation as well. 


## Installing and Running
As soon as you clone this repo, you need to create docker image and docker container, based on **Dockerfile**:
```bash
$ docker build -t flask_mongodb_app:latest .
```
Instead of "flask_mongodb_app" you can paste any name of the image you want. Once image is created, run a container:
```bash
$ docker run -it --env-file .env -p 5000:5000 -d flask_mongodb_app
```
Inside **.env** file the connection string to mongoDB service with my auth data provided.

**Keep in Mind.** Your app will be ran as a demon. You can make queries to the app and everything will be worked. But if you need to shutdown this demon, you can stop the container using command:

```bash
$ docker stop <container_id>
```

## Test requests

```bash
curl -H "Accept:application/json" http://127.0.0.1:5000/heroes
```

```bash
curl -i -X DELETE http://127.0.0.1:5000/hero/delete/Test123
 ```

```bash
curl -i -X POST -H "Content-Type:application/json" http://127.0.0.1:5000/hero/add -d '{
    "actor_name": "Test123",
    "hero_name": "Test123",
    "hero_rate": -1
}'
```

```bash
curl -i -X PUT -H "Content-Type:application/json" http://127.0.0.1:5000/hero/update/Test123 -d '{
    "actor_name": "Test",
    "hero_name": "Test",
    "hero_rate": 0
}' 
```