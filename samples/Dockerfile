# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
COPY . /usr/local/bin/
COPY . .


WORKDIR /samples
COPY . /samples

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


# Add this:
ENV FLASK_APP=app.py


#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
CMD ["gunicorn", "--conf", "gunicorn_config.py", "--bind", "0.0.0.0:5000", "app:app"]