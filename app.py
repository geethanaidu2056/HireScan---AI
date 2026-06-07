from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

# -------------------------
# HOME PAGE
# -------------------------
@app.route('/')
def home():
    return render_template("index.html")


# -------------------------
# RESUME ANALYZER (UPLOAD PDF)
# -------------------------
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['resume']

    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text().lower()

    # -------------------------
    # SKILL DATABASE
    # -------------------------
    skills = {
        "python": 20,
        "java": 20,
        "sql": 15,
        "html": 10,
        "css": 10,
        "javascript": 15,
        "django": 10
    }

    score = 0
    found_skills = []

    for skill, value in skills.items():
        if skill in text:
            score += value
            found_skills.append(skill)

    missing_skills = [s for s in skills if s not in found_skills]

    ats_percentage = round((len(found_skills) / len(skills)) * 100, 2)

    # -------------------------
    # JOB RECOMMENDATION
    # -------------------------
    job_roles = []

    if "python" in found_skills:
        job_roles.append("Backend Developer / Python Developer")

    if "java" in found_skills:
        job_roles.append("Software Developer (Java)")

    if "sql" in found_skills:
        job_roles.append("Data Analyst")

    if "javascript" in found_skills:
        job_roles.append("Frontend Developer")

    if score >= 80:
        job_roles.append("Full Stack Developer (Eligible)")

    if score < 50:
        job_roles.append("Internship / Skill Improvement Recommended")

    # -------------------------
    # IMPROVEMENT SUGGESTIONS
    # -------------------------
    suggestions = []

    if "html" not in found_skills:
        suggestions.append("Learn HTML for frontend development")

    if "css" not in found_skills:
        suggestions.append("Learn CSS for UI design skills")

    if "javascript" not in found_skills:
        suggestions.append("Learn JavaScript for frontend development")

    if "django" not in found_skills:
        suggestions.append("Learn Django for backend development")

    if score < 60:
        suggestions.append("Improve core programming + DSA skills")

    return render_template(
        "result.html",
        text=text,
        score=score,
        skills=found_skills,
        missing=missing_skills,
        jobs=job_roles,
        ats=ats_percentage,
        suggestions=suggestions
    )


# -------------------------
# RESUME BUILDER PAGE
# -------------------------
@app.route('/builder')
def builder():
    return render_template("builder.html")


# -------------------------
# GENERATE RESUME (TEMPLATE 1)
# -------------------------
@app.route('/generate', methods=['POST'])
def generate():
    data = request.form

    return render_template(
        "resume1.html",
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        skills=data['skills'],
        projects=data['projects']
    )


# -------------------------
# GENERATE RESUME (TEMPLATE 2)
# -------------------------
@app.route('/generate2', methods=['POST'])
def generate2():
    data = request.form

    return render_template(
        "resume2.html",
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        skills=data['skills'],
        projects=data['projects']
    )


# -------------------------
# RUN APP
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)