from parser.extract_text import extract_resume_text, parse_resume_text

file_path = "uploads/sample_resume.pdf"
resume_text = extract_resume_text(file_path)
parsed = parse_resume_text(resume_text)

print("Structured Resume Data:\n")
for key, value in parsed.items():
    print(f"{key.upper()}:\n{value}\n")
