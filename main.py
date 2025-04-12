# jobmatcher/main.py
from src.resume_parser import get_resume_embedding
from src.job_matcher import match_jobs_to_resume
from src.job_scraper_factory import get_scraper
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def export_to_gsheet(df, sheet_name="JobMatches"):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # Try to open or create the spreadsheet
    try:
        sheet = client.open(sheet_name).sheet1
    except gspread.SpreadsheetNotFound:
        sheet = client.create(sheet_name).sheet1

    sheet.clear()  # Clear existing content
    sheet.insert_row(df.columns.tolist(), index=1)
    for idx, row in df.iterrows():
        sheet.insert_row(row.tolist(), index=idx + 2)


if __name__ == '__main__':
    print("Loading resume...")
    resume_text = get_resume_embedding("data/resume.txt")

    # Choose job source here: 'remoteok', 'adzuna', 'wellfound', etc.
    job_source = 'remoteok'
    scraper = get_scraper(job_source)

    print(f"Scraping jobs from {job_source.title()}...")
    jobs = scraper(query="automation engineer")

    if not jobs:
        print("No jobs found. Exiting.")
        exit(1)

    print("Matching jobs to your resume...")
    matched_jobs = match_jobs_to_resume(resume_text, jobs)

    print("Saving top matches to data/jobs.csv...")
    matched_jobs.to_csv("data/jobs.csv", index=False)

    print("Exporting to Google Sheets...")
    export_to_gsheet(matched_jobs)
    print("Done.")
