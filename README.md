# Module 4 — Docker & Containerization

## Project Overview

This project demonstrates the fundamentals of Docker and containerization.

The project containerizes a Python Flask web application and uses Docker Compose to run the web application with PostgreSQL.

## Objectives

- Understand containers vs virtual machines
- Understand Docker architecture
- Learn Docker images and containers
- Create and use a Dockerfile
- Build Docker images
- Run Docker containers
- Understand Docker networking
- Use Docker volumes for persistent data
- Use environment variables
- Use Docker Compose
- Apply basic Dockerfile optimization

## Architecture

```text
Python Flask Application
          |
      Dockerfile
          |
     Docker Image
          |
   Flask Container
          |
    Docker Compose
       /       \
    Flask    PostgreSQL
       \       /
      Docker Network
          |
     Docker Volume

Technologies
- Docker
- Docker Compose
- Python
- Flask
- PostgreSQL
- Windows 11
- WSL 2


Project Structure
module-4-docker/
├── app.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
├── .env.example
├── README.md
└── screenshots/

Dockerfile
The Dockerfile uses a lightweight Python image, installs the required dependencies, copies the application, exposes port 5000, and starts the Flask application.

Docker Networking
Docker Compose provides a network that allows the Flask web service to communicate with PostgreSQL.
The Flask application uses the service name db as the database host.

Docker Volumes
PostgreSQL uses a named Docker volume for persistent database storage.

Environment Variables
Database configuration is passed using environment variables such as:
- DB_HOST
- DB_PORT
- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD

Real secrets are not committed to the repository.

Docker Compose
Docker Compose manages the Flask and PostgreSQL services together.

Start the project:
    docker compose up --build

Stop the project:
    docker compose down

Application
Open:
    http://localhost:5000

Database connectivity test:
    http://localhost:5000/db-test

Useful Docker Commands
    docker --version
    docker compose version
    docker images
    docker ps
    docker ps -a
    docker build -t module4-flask .
    docker run -d --name module4-web -p 5000:5000 module4-flask
    docker logs module4-web
    docker stop module4-web
    docker start module4-web
    docker rm module4-web
    docker network ls
    docker volume ls
    docker compose up --build
    docker compose ps
    docker compose down
    Dockerfile Optimization

The project uses:
- A slim Python base image
- .dockerignore
- Docker build cache-friendly layer ordering
- pip --no-cache-dir
- Only required dependencies

Learning Outcomes
After completing this project, I understand the basic Docker workflow:
Source Code → Dockerfile → Image → Container → Docker Compose → Running Application
I also practiced Docker networking, persistent volumes, environment variables, and containerized application deployment.
