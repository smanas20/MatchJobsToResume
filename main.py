from src.resume_parser import get_resume_embedding
from src.job_scraper import scrape_indeed_jobs
from src.job_matcher import match_jobs_to_resume
import pandas as pd

if __name__ == '__main__':
    print("Loading resume...")
    resume_text = get_resume_embedding("data/resume.txt")

    print("Scraping jobs from Indeed...")
    jobs = scrape_indeed_jobs(query="automation engineer", location="United States", max_results=50)

    print("Matching jobs to your resume...")
    matched_jobs = match_jobs_to_resume(resume_text, jobs)

    print("Saving top matches to data/jobs.csv...")
    matched_jobs.to_csv("data/jobs.csv", index=False)
    print("Done.")
