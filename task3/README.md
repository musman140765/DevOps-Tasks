# Flask + Redis App (Dockerized)

## Overview
A simple Python Flask application that connects to Redis and reads a dummy key called `message`. If the key doesn't exist, it sets the value to "Hello, World!".

## Components
- **Flask App**: Reads/writes to Redis
- **Redis**: In-memory database used as a key-value store
- **Dockerfile**: Builds the Flask container
- **docker-compose.yml**: Brings up both the app and Redis

## Prerequisites
- Docker and Docker Compose installed on your system

## How to Run

1. Clone the project and navigate into the folder:
   ```bash
   https://github.com/musman140765/DevOps-Tasks.git
   cd task2

