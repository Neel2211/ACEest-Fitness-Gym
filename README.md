# ACEest Fitness & Gym

## Project Overview

ACEest Fitness & Gym is a Flask-based fitness management application developed as part of the Introduction to DevOps course assignment.

The application provides APIs for:

- Client Management
- Workout Tracking
- Fitness Program Generation
- Membership Tracking

---

## Technologies Used

- Python
- Flask
- Pytest
- Docker
- GitHub Actions
- Jenkins

---

## Repository Structure

```text
ACEest-Fitness-Gym/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── README.md
│
├── tests/
│   └── test_app.py
│
└── .github/
    └── workflows/
        └── main.yml
```

---

## Local Setup

Clone repository:

```bash
git clone <repository-url>
```

Move into project directory:

```bash
cd ACEest-Fitness-Gym
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Application will start on:

```text
http://localhost:5000
```

---

## Run Tests

```bash
pytest
```

---

## Build Docker Image

```bash
docker build -t aceest-gym .
```

---

## Run Docker Container

```bash
docker run -p 5000:5000 aceest-gym
```

---

## GitHub Actions Workflow

The workflow executes automatically on every:

- Push
- Pull Request

Stages:

1. Checkout Source Code
2. Install Dependencies
3. Run Pytest
4. Build Docker Image

---

## Jenkins Integration

Jenkins performs:

1. Source Code Checkout from GitHub
2. Dependency Installation
3. Automated Testing using Pytest
4. Docker Image Build

---

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | / | Application Status |
| GET | /clients | Get All Clients |
| POST | /clients | Add New Client |
| GET | /clients/<name> | Get Client Details |
| GET | /programs | View Available Programs |
| POST | /generate_program/<name> | Generate Fitness Program |
| GET | /membership/<name> | Membership Status |
| POST | /workouts | Add Workout |
| GET | /workouts/<name> | Get Workout History |
