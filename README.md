# 🚀 PromptPilot AI

An AI-powered prompt optimization platform that transforms vague user queries into precise, context-rich, and high-quality prompts for AI models like ChatGPT, Gemini, Claude, and other LLMs.

---

## 🌐 Live Demo

### Backend API

https://promptpilot-ai-d46a.onrender.com

### Swagger API Documentation

https://promptpilot-ai-d46a.onrender.com/docs

---

## 📌 Overview

PromptPilot AI helps users generate effective prompts by converting simple or unclear queries into detailed, structured, and optimized prompts.

The application uses Google's Gemini API to enhance prompt quality and provides additional features such as prompt history, analytics, search, authentication, and Dockerized deployment.

---

## ✨ Features

* 🤖 AI-powered prompt optimization using Gemini API
* 📝 Generate detailed and structured prompts
* 📊 Prompt quality scoring
* 💾 Store prompt history using SQLite
* 🔍 Search previously generated prompts
* 🗑️ Delete saved prompts
* 👤 User Signup & Login
* 🔐 JWT-based Authentication
* 📈 Analytics API
* 🌐 REST API built with FastAPI
* 🐳 Docker support for containerized deployment
* ☁️ Cloud deployment on Render
* 📖 Interactive Swagger API documentation

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

### DevOps & Deployment

* Docker
* Render
* Git
* GitHub

### Additional Tools

* Uvicorn
* Swagger UI
* Pydantic
* python-dotenv

---

## 📂 Project Structure

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
├── render.yaml
├── .dockerignore
├── .gitignore
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/arjunkumar24b/promptpilot-ai.git

cd promptpilot-ai
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / MacOS

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Generate your Gemini API key from:

https://aistudio.google.com/app/apikey

---

## ▶️ Run Locally

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t promptpilot-ai .
```

### Run Docker Container

```bash
docker run -p 8000:8000 promptpilot-ai
```

---

## ☁️ Render Deployment

PromptPilot AI is deployed on Render.

Live API:

https://promptpilot-ai-d46a.onrender.com

API Docs:

https://promptpilot-ai-d46a.onrender.com/docs

---

## 📌 API Endpoints

| Method | Endpoint               | Description               |
| ------ | ---------------------- | ------------------------- |
| GET    | `/`                    | Welcome Endpoint          |
| GET    | `/health`              | Health Check              |
| POST   | `/signup`              | Register User             |
| POST   | `/login`               | User Login                |
| POST   | `/optimize`            | Generate Optimized Prompt |
| GET    | `/history`             | Get Prompt History        |
| GET    | `/search`              | Search Prompts            |
| DELETE | `/history/{prompt_id}` | Delete Prompt             |
| GET    | `/analytics`           | Prompt Analytics          |

---

## 🔄 Application Workflow

1. User enters a query.
2. FastAPI receives the request.
3. Gemini API optimizes the prompt.
4. Prompt quality score is calculated.
5. Prompt data is stored in SQLite.
6. Users can search, view, or delete prompts.

---

## 📸 Screenshots

### API Documentation

![Swagger UI](screenshots/docs.png)

---

### Prompt Generation Interface

![Frontend](screenshots/home.png)

---

### Optimized Prompt Example

![Result](screenshots/result.png)

---

## 🚀 Future Enhancements

* User-specific prompt history
* React frontend
* Frontend deployment on Vercel
* Export prompts as PDF
* Rate limiting
* Prompt templates marketplace
* CI/CD pipeline
* Role-based authentication

---

## 👨‍💻 Author

**Arjun Kumar**

GitHub: https://github.com/arjunkumar24b

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
