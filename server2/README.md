# Server

## Please keep in mind that the first request can take more than 5 minutes(it depends on the speed of your internet) because of nltk packages and TensorFlow pre-trained models, they have more than 500 Mb.

## Local running:
### gunicorn, please type command: 
1. gunicorn app:app -b 0.0.0.0:5000 -c gunicorn.config.py

### docker, please build and run docker (flask + gunicorn):
1. docker build . -t server
2. docker run -p 5000:5000 server