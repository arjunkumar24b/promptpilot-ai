# 🚀 PromptPilot AI

An AI-powered prompt optimization platform that transforms vague user queries into precise, high-quality prompts for Large Language Models (LLMs) like ChatGPT, Gemini, and Claude.

---

# 📌 Overview

PromptPilot AI helps users generate better prompts for AI platforms by converting simple or unclear user inputs into detailed, context-rich prompts. The system also provides prompt quality analysis, history management, and analytics.

---

# ✨ Features

* 🤖 AI-powered prompt optimization using Gemini API
* 📝 Generate detailed and structured prompts
* 📊 Prompt quality scoring system
* 💾 Save prompt history in SQLite database
* 🔍 Search previously generated prompts
* 🗑️ Delete prompt history
* 👤 User Signup and Login
* 🔐 JWT-based Authentication
* 📈 Analytics API for prompt statistics
* 🌐 REST API built with FastAPI
* 🐳 Docker support for containerized deployment
* 📖 Interactive Swagger API documentation

---

# 🛠️ Tech Stack

## Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Gemini API
* JWT Authentication
* Passlib (bcrypt)

## Frontend

* HTML
* CSS
* JavaScript

## DevOps & Tools

* Docker
* Git
* GitHub
* Uvicorn
* Swagger UI

---

# 📂 Project Structure

```text
promptpilot-ai/

├── app/
│   ├── auth.py
│   ├── crud.py
│   ├── database.py
│   ├── gemini_service.py
│   ├── main.py
│   ├── models.py
│   ├── prompt_engine.py
│   ├── schemas.py
│   ├── scorer.py
│   ├── security.py
│   └── templates.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── screenshots/
│   ├── docs.png
│   ├── home.png
│   └── result.png
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/arjunkumar24b/promptpilot-ai.git

cd promptpilot-ai
```

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

## 3. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Gemini API

Open:

```text
app/gemini_service.py
```

Replace:

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

with your own Gemini API key.

You can generate a key from:

https://aistudio.google.com/app/apikey

---

# ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🐳 Docker Support

## Build Docker Image

```bash
docker build -t promptpilot-ai .
```

## Run Docker Container

```bash
docker run -p 8000:8000 promptpilot-ai
```

---

# 📌 API Endpoints

| Method | Endpoint      | Description               |
| ------ | ------------- | ------------------------- |
| GET    | /             | Welcome Endpoint          |
| GET    | /health       | Health Check              |
| POST   | /signup       | Register User             |
| POST   | /login        | User Login                |
| POST   | /optimize     | Generate Optimized Prompt |
| GET    | /history      | Get Prompt History        |
| GET    | /search       | Search Prompts            |
| DELETE | /history/{id} | Delete Prompt             |
| GET    | /analytics    | Prompt Analytics          |

---

# 🧠 Example Workflow

1. User enters a query.
2. PromptPilot AI receives the request.
3. Gemini API generates an optimized prompt.
4. The system calculates a quality score.
5. Prompt data is stored in SQLite.
6. User can search, view, or delete previous prompts.

---

# 📸 Screenshots

## API Documentation

![Swagger UI](screenshots/docs.png)

---

## Prompt Generation Interface

![Frontend](screenshots/home.png)

---

## Optimized Prompt Example

![Result](screenshots/result.png)

---

# 🚀 Future Enhancements

* User-specific prompt history
* React frontend
* Deployment on Render and Vercel
* Export prompts as PDF
* Prompt templates marketplace
* Rate limiting
* CI/CD pipeline
* Role-based authentication

---

# 👨‍💻 Author

**Arjun Kumar**

GitHub: https://github.com/arjunkumar24b

---

# ⭐ If you like this project, give it a star!
