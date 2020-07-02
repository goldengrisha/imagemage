FROM python:3.8-slim
EXPOSE 5000


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt update
RUN pip3 install -r requirements.txt

COPY . /app


CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "-c", "gunicorn.config.py"]
# here is commands for proper running
# docker build . -t server
# docker run -p 5000:5000 server
