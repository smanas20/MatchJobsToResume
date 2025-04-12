import requests
from bs4 import BeautifulSoup
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_indeed_jobs(query, location="United States", max_results=50):
    query = query.replace(" ", "+")
    location = location.replace(" ", "+")
    jobs = []
    start = 0

    while len(jobs) < max_results:
        url = f"https://www.indeed.com/jobs?q={query}&l={location}&start={start}"
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all("div", class_="job_seen_beacon")

        if not cards:
            break

        for card in cards:
            title_tag = card.find("h2", class_="jobTitle")
            title = title_tag.text.strip() if title_tag else "N/A"
            company_tag = card.find("span", class_="companyName")
            company = company_tag.text.strip() if company_tag else "N/A"
            summary_tag = card.find("div", class_="job-snippet")
            summary = summary_tag.text.strip().replace("\n", " ") if summary_tag else "N/A"
            link = "https://www.indeed.com" + title_tag.find("a")["href"] if title_tag and title_tag.find("a") else "N/A"

            jobs.append({
                "title": title,
                "company": company,
                "description": summary,
                "link": link
            })

            if len(jobs) >= max_results:
                break

        start += 10
        time.sleep(1)

    return jobs
