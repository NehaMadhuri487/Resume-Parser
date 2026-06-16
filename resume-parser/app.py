import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from parser.extract_text import extract_resume_text, parse_resume_text
from skill_extractor import load_skills, detect_skills_by_category

app = Flask(__name__)
app.secret_key = "resume_parser_secret"

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
ALLOWED_EXTENSIONS = {"pdf", "docx"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part in request")
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            flash("No file selected")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            # Step 1: Extract resume text
            resume_text = extract_resume_text(filepath)

            # Step 2: Parse structured sections
            parsed_sections = parse_resume_text(resume_text)

            # Step 3: Detect skills by category
            skills_data = load_skills("skills_dataset.csv")
            detected_skills = detect_skills_by_category(resume_text, skills_data)

            # Step 4: Render results page
            return render_template(
                "result.html",
                sections=parsed_sections,
                skills=detected_skills
            )
        else:
            flash("Invalid file type. Only PDF/DOCX allowed.")
            return redirect(request.url)

    return render_template("index.html")

from flask import send_file
import io

@app.route("/download", methods=["POST"])
def download_resume():
    # Get resume text from form submission
    resume_text = request.form.get("resume_text", "")

    # Create a text file in memory
    buffer = io.BytesIO()
    buffer.write(resume_text.encode("utf-8"))
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="extracted_resume.txt",
        mimetype="text/plain"
    )


if __name__ == "__main__":
    app.run(debug=True)

