#!/bin/bash

mkdir -p producer consumer frontend

touch producer/Dockerfile producer/producer.py producer/requirements.txt
touch consumer/Dockerfile consumer/consumer.py consumer/requirements.txt
touch frontend/Dockerfile frontend/kafka.js frontend/package.json

echo "Directory tree created successfully."

