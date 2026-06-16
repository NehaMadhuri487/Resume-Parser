import pdfplumber
import docx
import re

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text.strip()

def extract_resume_text(file_path):
    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Only PDF/DOCX allowed.")

def parse_resume_text(text):
    sections = {}
    lines = text.splitlines()

    # Regex patterns for personal info
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"\+?\d[\d\s-]{8,}\d"
    github_pattern = r"(https?://)?(www\.)?github\.com/[A-Za-z0-9_-]+"
    linkedin_pattern = r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+"

    # Extract email
    email_match = re.search(email_pattern, text)
    if email_match:
        sections["Email"] = email_match.group()

    # Extract phone
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        sections["Phone"] = phone_match.group()

    # Extract GitHub
    github_match = re.search(github_pattern, text)
    if github_match:
        sections["GitHub"] = github_match.group()

    # Extract LinkedIn
    linkedin_match = re.search(linkedin_pattern, text)
    if linkedin_match:
        sections["LinkedIn"] = linkedin_match.group()

    # Try to capture name (often first line)
    first_line = lines[0].strip()
    if re.match(r"^[A-Z][a-zA-Z]+(?:\s[A-Z][a-zA-Z]+)*$", first_line):
        sections["Name"] = first_line

    # Resume headings
    headings = [
        "Education",
        "Skills",
        "Experience",
        "Projects",
        "Certifications",
        "Certifications & Learning",
        "Achievements"
    ]

    current_heading = None
    buffer = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        if any(stripped.lower().startswith(h.lower()) for h in headings):
            if current_heading:
                sections[current_heading] = "\n".join(buffer).strip()
                buffer = []
            current_heading = stripped.split()[0]
        else:
            if current_heading:
                buffer.append(stripped)

    if current_heading and buffer:
        sections[current_heading] = "\n".join(buffer).strip()

    return sections
