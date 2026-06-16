# Resume-Parser

## 📌 Intern Details

* **Intern ID:** CITS1931
* **Full Name:** Boddu Neha Madhuri
* **Project Name:** Resume Parser
* **Duration:** 6 Weeks
* **Project Scope:** Develop an AI-assisted resume parsing system capable of extracting text from PDF and DOCX resumes, identifying personal and professional information, categorizing skills using dataset-based analysis, and presenting structured resume insights through a Flask web application interface.

---

# 📖 Project Overview

The AI Resume Parser is a web-based application developed using Flask that automatically extracts and organizes information from resumes uploaded in PDF and DOCX formats.

The system processes resumes by extracting text content, identifying important personal details, categorizing skills, and presenting structured output through a user-friendly interface.

This project demonstrates document processing, resume parsing, text extraction, and skill analysis techniques.

---

# 🎯 Project Objectives

* Upload and process resumes in PDF and DOCX formats.
* Extract text automatically from resumes.
* Identify personal information such as:

  * Name
  * Email
  * Phone Number
  * GitHub Profile
  * LinkedIn Profile
* Detect resume sections:

  * Education
  * Skills
  * Experience
  * Projects
  * Certifications
  * Achievements
* Categorize technical skills using a predefined dataset.
* Display structured resume information through a web interface.
* Allow users to download extracted resume content.

---

# 🛠️ Technologies Used

### Frontend

* HTML
* CSS
* Jinja Templates

### Backend

* Python
* Flask

### Libraries

* pdfplumber
* python-docx
* pandas
* werkzeug
* re (Regular Expressions)

---

# 📂 Project Structure

```plaintext
AI-Resume-Parser/
│
├── app.py
├── skill_extractor.py
├── skills_dataset.csv
│
├── parser/
│   └── extract_text.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── uploads/
│
├── test_extractor.py
├── test_skill.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Working Procedure

## Step 1: Upload Resume

The user uploads a resume file in PDF or DOCX format.

↓

## Step 2: Resume Text Extraction

The system extracts textual content from uploaded resumes using:

* pdfplumber
* python-docx

↓

## Step 3: Resume Parsing

The extracted content is analyzed to identify:

* Name
* Email
* Phone Number
* GitHub
* LinkedIn
* Resume Sections

↓

## Step 4: Skill Detection

Skills are matched against the dataset and grouped into categories.

↓

## Step 5: Display Results

Structured information is displayed on the result page.

↓

## Step 6: Download Extracted Resume

Users can download extracted text as a `.txt` file.

---

# 🚀 Installation & Execution

## 1️⃣ Clone Repository

```bash
git clone https://github.com/NehaMadhuri487/Resume-Parser
```

## 2️⃣ Move into Project Folder

```bash
cd AI-Resume-Parser
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Run Application

```bash
python app.py
```

---

# 🌐 Open in Browser

```plaintext
http://127.0.0.1:5000
```

---

# 🧪 Testing Files

Run Resume Extraction Test:

```bash
python test_extractor.py
```

Run Skill Detection Test:

```bash
python test_skill.py
```

---

# 📌 Key Features

✔ Resume Upload (PDF/DOCX)
✔ Text Extraction
✔ Structured Resume Parsing
✔ Skill Categorization
✔ Contact Information Extraction
✔ Download Extracted Content
✔ Flask-Based Web Application

---

# 📈 Future Enhancements

* OpenAI API Integration for intelligent resume understanding
* ATS Score Calculation
* Resume vs Job Description Matching
* Resume Analytics Dashboard
* Database Integration
* AI Skill Recommendations

---

# ✅ Conclusion

The AI Resume Parser successfully automates resume analysis by extracting and organizing resume information into structured sections. The application reduces manual effort and provides a scalable foundation for future AI-powered recruitment and resume evaluation systems.
