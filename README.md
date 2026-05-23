🚀 Cloud With Nidhi

A simple Flask application built using Python and deployed using a complete DevOps workflow with Docker and Jenkins CI/CD Pipeline.

👩‍💻 About The Project

Hi, I am Nidhi Mishra, a Software Engineer at HCL Software.

This project demonstrates a basic cloud-native deployment workflow where:

A Flask application is developed using Python
Docker is used for containerization
Jenkins is used to automate build, push, and deployment processes
GitHub is used for version control and Multibranch Pipeline integration
🛠️ Tech Stack
Python
Flask
Docker
Jenkins
GitHub
CI/CD Pipeline
📂 Project Structure
project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md
⚙️ Flask Application

The Flask application exposes a simple API endpoint:

GET /

Example response:

{
  "owner": "Nidhi Mishra",
  "role": "Software Engineer at HCL Software",
  "message": "✨ Welcome to Cloud with Nidhi ✨",
  "deployment": "Built with Flask, containerized using Docker, and deployed via Jenkins Pipeline 🚀"
}
🐳 Docker Setup
Build Docker Image
docker build -t nidhi-flaskpipeline .
Run Container
docker run -d -p 5000:5000 --name flaskapp nidhi-flaskpipeline
🔄 Jenkins CI/CD Pipeline

The Jenkins pipeline automates:

Source Code Checkout
Docker Image Build
DockerHub Push
Container Deployment
Application Testing
Pipeline Flow
GitHub → Jenkins → Docker Build → DockerHub Push → Deploy Container
🌐 Access Application

Once deployed:

http://localhost:5000
📌 Features
Simple Flask REST API
Dockerized application
Automated CI/CD pipeline
Multibranch Pipeline support
DockerHub image publishing
Jenkins deployment automation
❤️ Author
Nidhi Mishra

Software Engineer at HCL Software

Built with Python, Docker, and Jenkins 🚀