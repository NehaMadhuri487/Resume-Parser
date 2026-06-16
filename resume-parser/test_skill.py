from parser.extract_text import extract_resume_text
from skill_extractor import load_skills, detect_skills_by_category

# Step 1: Extract text from resume
file_path = "uploads/sample_resume.pdf"   # or .docx
resume_text = extract_resume_text(file_path)

# Step 2: Load skills dataset
skills_data = load_skills("skills_dataset.csv")

# Step 3: Detect skills by category
detected = detect_skills_by_category(resume_text, skills_data)

# Step 4: Print results
print("Detected Skills by Category:\n")
for category, skills in detected.items():
    print(f"{category}:")
    for skill in skills:
        print(f"  - {skill}")
    print()
