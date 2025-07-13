# 🚀 Vaibhavi Flask DevOps Project

This project is a basic **Flask web app** created for DevOps learning. It includes:

- Simple web pages (About Me, Skills, Projects, Contact)
- Test cases using `pytest`
- Dockerfile to containerize the app
- CI pipeline using Jenkins (Clone ➜ Test ➜ Docker Build)

---

## 📁 Project Structure

vaibhavi-flask-app/
│
├── app.py # Flask web application
├── test_app.py # Pytest test cases
├── Dockerfile # Dockerfile to containerize app
└── Jenkinsfile # Jenkins Pipeline script (CI)


---

## 🧑‍🍳 How to Run This Flask App (Locally)

### 1. Install Flask


pip install flask

 Run the app
 python app.py
Open your browser and go to:
👉 http://localhost:5000

🐳 Run Flask App Using Docker
1. Build Docker Image

docker build -t vaibhavi-flask-app .

 Run Docker Container
 docker run -d -p 5000:5000 vaibhavi-flask-app

Go to: http://localhost:5000

🧪 Run Test Cases using Pytest
1. Install pytest
pip install pytest

Run Tests
pytest test_app.py

You will see test results for all routes.

🛠️ Jenkins Setup Steps
Login to Jenkins

Create a New Item → Select Pipeline

Configure SCM (GitHub Repo):

URL: Your Github repo 

Branch: main

Credentials: GitHub token (added in Jenkins)

Use Jenkinsfile from repo

Click Build Now

🧪 Jenkinsfile Pipeline Steps:
✅ Clone repo
✅ Install Flask & pytest
✅ Run tests
✅ Build Docker image
✅ Show image in Docker


👨‍💻 Author
Made with ❤️ by Sumit Tiwari