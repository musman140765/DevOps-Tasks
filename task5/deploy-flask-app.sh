#!/bin/bash

REPO_URL="https://github.com/musman140765/DevOps-Tasks.git"

echo "Updating the system and installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y \
  docker.io \
  docker-compose \
  git \
  curl

echo "Starting Docker service..."
sudo systemctl enable docker
sudo systemctl start docker

echo "Cloning the repository..."
git clone $REPO_URL $TARGET_DIR

cd /home/ubuntu/DevOps-Tasks/task3

echo "Building and running the Docker containers using Docker Compose..."
sudo docker-compose up -d --build

echo "Checking Docker Compose logs"
sudo docker-compose logs -f

