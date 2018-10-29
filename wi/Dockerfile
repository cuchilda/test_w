# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.6

# The enviroment variable ensures that the python output is set straight to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /test_w

# Set the working directory to /music_service
WORKDIR /test_w


# Copy the current directory contents into the container at /music_service
ADD . /test_w

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

