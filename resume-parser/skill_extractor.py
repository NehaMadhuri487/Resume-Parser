import pandas as pd

def load_skills(csv_path="skills_dataset.csv"):
    """Load skills and categories from CSV."""
    df = pd.read_csv(csv_path)
    # Expect columns: skill, category
    skills = [(row['skill'].lower().strip(), row['category']) for _, row in df.iterrows()]
    return skills

def detect_skills_by_category(resume_text, skills_data):
    """Detect skills and group them into categories based on CSV mapping."""
    resume_lower = resume_text.lower()
    categories = {}

    for skill, category in skills_data:
        if skill in resume_lower:
            categories.setdefault(category, []).append(skill)

    return categories
