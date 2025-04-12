from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def match_jobs_to_resume(resume_text, jobs):
    job_texts = [job["description"] for job in jobs]
    titles = [job["title"] for job in jobs]
    companies = [job["company"] for job in jobs]
    links = [job["link"] for job in jobs]

    corpus = [resume_text] + job_texts
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    df = pd.DataFrame({
        "Job Title": titles,
        "Company": companies,
        "Similarity Score": similarities,
        "Job Link": links
    })

    return df.sort_values(by="Similarity Score", ascending=False).reset_index(drop=True)
