# python base image in the container from Docker Hub
FROM python:3.7.9-slim


# copy files to the /src folder in the container
COPY . /src

# set the working directory in the container to be /src
WORKDIR /src
#COPY ./requirements.txt /src/requirements.txt

#RUN dir

# install the packages from the Pipfile in the container
#RUN pip install -r requirements.txt

# expose the port that uvicorn will run the app on
ENV PORT=8000
EXPOSE 8000

# execute the command python main.py (in the WORKDIR) to start the app
CMD ["python", "function.py"]