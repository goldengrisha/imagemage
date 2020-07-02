from os import environ
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

with app.app_context():
    import routes

app.config['CELERY_BROKER_URL'] = 'http://127.0.0.1:6379'
app.config['CELERY_RESULT_BACKEND'] = 'http://127.0.0.1:6379'


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)
