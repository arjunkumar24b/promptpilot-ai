# 🚀 PromptPilot AI

## Overview

PromptPilot AI is an AI-powered prompt optimization platform that transforms vague user queries into highly effective, context-rich prompts for Large Language Models (LLMs) such as ChatGPT, Gemini, and Claude.

The application helps users generate precise prompts, improve response quality, and reduce the number of iterations required to get accurate AI-generated answers.

---

## ✨ Features

* 🤖 AI-powered prompt optimization using Gemini API
* 📈 Prompt quality scoring system
* 📝 Prompt history management
* 🔍 Search previously generated prompts
* 🗑️ Delete prompt history
* 👤 User authentication (Signup/Login)
* 🔐 JWT-based authentication
* 💾 SQLite database integration
* 📊 Analytics dashboard API
* 🌐 FastAPI backend with REST APIs
* 🎨 Interactive frontend interface

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Gemini API
* JWT Authentication
* Passlib (bcrypt)

### Frontend

* HTML
* CSS
* JavaScript

### Other Tools

* Git & GitHub
* Uvicorn
* Swagger UI

---

## 📁 Project Structure

```text
promptpilot-ai/

├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   ├── security.py
│   ├── scorer.py
│   ├── gemini_service.py
│   ├── prompt_engine.py
│   └── templates.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/arjunkumar24b/promptpilot-ai.git

cd promptpilot-ai
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Open:

```text
app/gemini_service.py
```

Replace:

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

with your own Gemini API key.

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints

| Method | Endpoint      | Description               |
| ------ | ------------- | ------------------------- |
| GET    | /             | Root Endpoint             |
| GET    | /health       | Health Check              |
| POST   | /signup       | User Registration         |
| POST   | /login        | User Login                |
| POST   | /optimize     | Generate Optimized Prompt |
| GET    | /history      | View Prompt History       |
| GET    | /search       | Search Prompts            |
| DELETE | /history/{id} | Delete Prompt             |
| GET    | /analytics    | View Analytics            |

---

## 🧠 Example Workflow

1. User enters a vague query.
2. PromptPilot sends the query to Gemini AI.
3. Gemini generates an optimized prompt.
4. The system calculates a quality score.
5. The prompt is stored in SQLite.
6. User can search, view, or delete prompt history.

---

## 🚀 Future Enhancements

* User-specific prompt history
* React frontend
* Docker support
* Deployment on Render/Vercel
* Prompt export as PDF
* Prompt templates marketplace
* Rate limiting
* CI/CD pipeline

---

## 👨‍💻 Author

**Arjun Kumar**

GitHub: https://github.com/arjunkumar24b

---

## ⭐ If you like this project, please give it a star!
