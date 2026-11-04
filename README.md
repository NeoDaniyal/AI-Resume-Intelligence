# 🚀 AI Resume Intelligence & Career Optimization Platform

An advanced, AI-powered recruitment and career intelligence platform designed to parse, analyze, screen, and optimize resumes using a combination of **Machine Learning (XGBoost/Scikit-learn)**, **Natural Language Processing (NLTK/spaCy)**, **Vector Embeddings**, and **Large Language Models**.

---

## 🏗️ System Architecture & Tech Stack

* **Frontend:** React + Vite, Tailwind CSS / Custom Styling, Axios, Lucide React
* **Backend:** FastAPI (Python), Uvicorn, Pydantic
* **Database & Storage:** MongoDB (PyMongo), FAISS Vector Store
* **ML & NLP Engine:** Scikit-learn, NLTK, spaCy, Sentence Transformers
* **Document Processing:** PyMuPDF (`fitz`), `python-docx`, ReportLab

---

## 📂 Project Folder Structure

```text
AI-Resume-Intelligence/
│
├── backend/
│   ├── app/
│   │   ├── main.py                # FastAPI entry point & lifespan events
│   │   ├── config.py              # Environment configuration
│   │   ├── routes/                # API Endpoints (resumes, screening, etc.)
│   │   ├── services/              # Business logic (parsers, cleaners)
│   │   ├── ml/                    # ML models, training, & preprocessing
│   │   ├── database/              # MongoDB connection & collections setup
│   │   └── utils/                 # File validators & helpers
│   ├── uploads/                   # Local storage for raw uploaded resumes
│   ├── requirements.txt           # Python dependencies
│   └── .env                       # Environment variables
│
├── frontend/
│   ├── src/
│   │   ├── components/            # Reusable UI components
│   │   ├── pages/                 # Application views/pages
│   │   ├── services/              # API communication layer (Axios)
│   │   ├── App.jsx                # Main React root component
│   │   └── main.jsx               # React DOM entry
│   └── package.json               # Node dependencies
│
├── datasets/                      # Training & evaluation datasets
├── notebooks/                     # Jupyter notebooks for experimentation
└── README.md                      # Project documentation