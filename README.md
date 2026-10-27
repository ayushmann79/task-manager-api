# Task Manager API

A simple REST API built with Python and Flask to manage tasks, featuring automated testing with pytest and Continuous Integration (CI) using GitHub Actions.

## Features

- Retrieve all tasks
- Create new tasks
- Validate task titles
- Automated API tests
- GitHub Actions CI pipeline

## Tech Stack

- Python 3.12
- Flask
- pytest
- GitHub Actions
- Git and GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/ayushmann79/task-manager-api.git
cd task-manager-api
```

Create and activate a virtual environment on Windows:

```powershell
python -m venv myVirtual
.\myVirtual\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

The API runs locally at `http://127.0.0.1:5000`.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/tasks` | Retrieve all tasks |
| POST | `/tasks` | Create a task |

Example request to create a task:

```json
{
  "title": "Learn GitHub Actions"
}
```

## Run Tests

```bash
python -m pytest -v
```

## CI Pipeline

GitHub Actions automatically installs dependencies and runs the test suite when code is pushed to `main` or a pull request targets `main`.

## Learning Objectives

This project demonstrates REST API development, automated testing, Git version control, YAML configuration, and CI/CD fundamentals.