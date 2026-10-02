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

## Version Control Strategy

The ACEest Fitness & Gym application was developed using an incremental versioning approach based on the supplied source code versions.

### Legacy Version Evolution

- ACEest v1.0
- ACEest v1.1
- ACEest v1.1.2
- ACEest v2.0.1
- ACEest v2.1.2
- ACEest v2.2.1
- ACEest v2.2.4
- ACEest v3.0.1
- ACEest v3.1.2
- ACEest v3.2.4

Each version was maintained in a dedicated Git branch to demonstrate version control practices and incremental software evolution.

### Feature Branches

The following feature branches were created to demonstrate a typical DevOps workflow:

- feature-flask
- feature-testing
- feature-docker
- feature-cicd
- feature-jenkins

### DevOps Implementation

The final implementation includes:

- Flask REST APIs
- Pytest automated testing
- Docker containerization
- GitHub Actions CI pipeline
- Jenkins build pipeline

All feature branches were merged into the main branch to simulate an enterprise software delivery workflow.
