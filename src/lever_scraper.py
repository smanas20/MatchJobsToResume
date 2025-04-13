# jobmatcher/src/lever_scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_lever_jobs(company="sambanova", query=None, max_results=50):
    url = f"https://jobs.lever.co/{company}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    listings = soup.select("div.posting")
    for job in listings:
        title = job.select_one("h5").text.strip()
        location = job.select_one("span.sort-by-location").text.strip()
        link = job.find("a")["href"]

        if query and query.lower() not in title.lower():
            continue

        jobs.append({
            "title": title,
            "company": company,
            "description": f"{title} - {location}",
            "link": link
        })

        if len(jobs) >= max_results:
            break

    return jobs
