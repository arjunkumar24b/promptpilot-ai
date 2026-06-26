# 🚀 PromptPilot AI

An AI-powered prompt optimization platform that transforms vague user queries into precise, context-rich, and high-quality prompts for AI models like ChatGPT, Gemini, Claude, and other Large Language Models (LLMs).

---

## 🌐 Live Demo

### Frontend Application

**Live Website:**  
https://your-vercel-url.vercel.app

### Backend API

**Render Backend:**  
https://promptpilot-ai-d46a.onrender.com

### Swagger Documentation

**API Docs:**  
https://promptpilot-ai-d46a.onrender.com/docs

---

## 📌 Overview

PromptPilot AI helps users generate effective prompts by converting simple or unclear queries into detailed, structured, and optimized prompts.

The application leverages Google's Gemini API to improve prompt quality and provides features such as:

- Prompt optimization
- Prompt history management
- Analytics dashboard
- Search functionality
- User authentication
- Cloud deployment

---

## ✨ Features

- 🤖 AI-powered prompt optimization using Gemini API
- 📝 Generate detailed and structured prompts
- 📊 Prompt quality scoring
- 💾 Store prompt history in SQLite
- 🔍 Search previously generated prompts
- 🗑️ Delete saved prompts
- 👤 User Signup & Login
- 🔐 JWT-based Authentication
- 📈 Prompt analytics
- 🌐 REST APIs built with FastAPI
- 🐳 Docker containerization
- ☁️ Cloud deployment on Render
- ▲ Frontend deployment on Vercel
- 📖 Interactive Swagger API documentation

---

## 🛠️ Tech Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Gemini API
- JWT Authentication
- Passlib (bcrypt)

### Frontend

- HTML5
- CSS3
- JavaScript

### DevOps & Deployment

- Docker
- Render
- Vercel
- Git
- GitHub

### Additional Libraries

- Pydantic
- Uvicorn
- python-dotenv
- Swagger UI

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
├── render.yaml
├── requirements.txt
├── README.md
├── .dockerignore
├── .gitignore
└── .env
```

---

## ⚙️ Local Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/arjunkumar24b/promptpilot-ai.git

cd promptpilot-ai
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
```

Generate your Gemini API key from:

https://aistudio.google.com/app/apikey

---

## ▶️ Run Locally

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Application URL:

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

## ☁️ Cloud Deployment

### Backend (Render)

https://promptpilot-ai-d46a.onrender.com

### Frontend (Vercel)

https://your-vercel-url.vercel.app

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome Endpoint |
| GET | `/health` | Health Check |
| POST | `/signup` | Register User |
| POST | `/login` | User Login |
| POST | `/optimize` | Generate Optimized Prompt |
| GET | `/history` | Get Prompt History |
| DELETE | `/history/{prompt_id}` | Delete Prompt |
| GET | `/search` | Search Prompts |
| GET | `/analytics` | Prompt Analytics |

---

## 🔄 Application Workflow

1. User enters a query.
2. Frontend sends request to FastAPI backend.
3. Backend invokes Gemini API.
4. Gemini generates an optimized prompt.
5. Quality score is calculated.
6. Prompt is stored in SQLite.
7. User can search, analyze, and manage prompt history.

---

## 📸 Screenshots

### API Documentation

![Swagger UI](screenshots/docs.png)

---

### Prompt Generation Interface

![Frontend](screenshots/home.png)

---

### Optimized Prompt Example

![Optimized Prompt](screenshots/result.png)

---

## 🚀 Future Enhancements

- 🌙 Dark mode
- 📋 Copy-to-clipboard button
- 📄 Export prompts as PDF
- ⚛️ React frontend
- 👥 User-specific dashboards
- 🔔 Notifications
- 🔄 CI/CD Pipeline
- 🧩 Prompt template marketplace

---

## 👨‍💻 Author

**Arjun Kumar**

GitHub: https://github.com/arjunkumar24b

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.

