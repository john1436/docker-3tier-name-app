### 📦 3-Tier Docker Application — Name Saver App

A simple 3-tier web application built using Docker, demonstrating how a frontend → backend → database architecture works inside containers.

This project stores names in a PostgreSQL database and retrieves them through a Flask API, all served via an Nginx frontend.

Perfect for DevOps learning, containers, networking, and portfolio demonstration.

### 🏗 Architecture Overview
                +------------------+
                |     Frontend     |
                |  (Nginx + HTML)  |
                |  Port: 8080      |
                +--------+---------+
                         |
                         v
                 http://backend:5000
                         |
                +--------+---------+
                |      Backend     |
                | (Flask API)      |
                | Port: 5000       |
                +--------+---------+
                         |
                         v
                +--------+---------+
                |     Database     |
                |  PostgreSQL 15   |
                | Port: 5432       |
                +------------------+


All containers communicate through the same Docker network: appnet.

### 🚀 Features
✔ Simple HTML UI

Enter a name → Save it → Fetch names.

### ✔ Flask Backend API

Endpoints:

POST /save → inserts name

GET /names → returns all names

### ✔ PostgreSQL Database

Stores names using a users table.

### ✔ Dockerized 3-tier architecture

frontend/ → Nginx serving static HTML

backend/ → Flask API + psycopg2 + CORS

db → PostgreSQL container

### 📁 Project Structure
app-3tier/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   └── Dockerfile
│
└── README.md

### 🐳 Docker Setup

Create a Docker network so containers can talk to each other:

docker network create appnet

### 🗄 Run PostgreSQL
docker run -d \
  --name db \
  --network appnet \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=mydb \
  postgres:15


### Create table:

docker exec -it db psql -U admin -d mydb \
  -c "CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT);"

### 🖥 Run Backend (Flask API)
cd backend
docker build -t backend-app .
docker run -d \
  --name backend \
  --network appnet \
  -p 5000:5000 \
  backend-app


### Test API:

curl http://localhost:5000/names

### 🌐 Run Frontend (Nginx)
cd frontend
docker build -t frontend-app .
docker run -d \
  --name frontend \
  --network appnet \
  -p 8080:80 \
  frontend-app


### Open in browser:

http://<EC2_PUBLIC_IP>:8080
