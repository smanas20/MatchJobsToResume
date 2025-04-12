def get_resume_embedding(resume_path):
    with open(resume_path, 'r', encoding='utf-8') as file:
        resume_text = file.read()
    return resume_text
