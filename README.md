# HireScan - AI 
# 🧠 AI Resume Analyzer + ATS Resume Builder

An AI-powered web application that analyzes resumes, calculates ATS compatibility score, recommends job roles, and also allows users to generate ATS-friendly resumes using templates.
---

## 📌 Features

### 📄 Resume Analyzer
- Upload PDF resume
- Extract text automatically
- Detect skills (Python, Java, SQL, etc.)
- Calculate ATS Match Score
- Identify missing skills
- Recommend job roles
- Provide improvement suggestions

### 🧠 AI Resume Builder
- Fill personal details
- Generate ATS-friendly resume
- Multiple resume templates
- Instant preview

---

## 🛠 Tech Stack

- Python
- Flask
- PyPDF2
- HTML
- CSS

---

## 📁 Project Architecture

- **Frontend:** HTML, CSS (Jinja Templates)
- **Backend:** Flask (Python)
- **AI Logic:** Rule-based ATS scoring system
- **File Processing:** PyPDF2 for resume parsing

### Folder Overview:
- `app.py` → Core backend logic
- `templates/` → UI pages
- `static/` → Styling and assets
- `screenshots/` → UI previews for GitHub