# Galaxy Classification App

## Description
This is an API that classifies images of galaxies. It is trained using SDSS data, and the classifier is a deep convolutional neural network. The API is built using FastAPI and the model is trained using Tensorflow. The API and the model are deployed using Docker and Docker Compose.

## Purpose
This was created to be a learning project for developing neural networks, building an API, and deploying both of them locally using Docker and the Tensorflow Serving Server. It is not a production-ready application.

### To run the project locally:
1. `docker-compose build`
2. `docker-compose up`
3. Navigate to `localhost:80` to see the API documentation

