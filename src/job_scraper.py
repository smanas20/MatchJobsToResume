# jobmatcher/src/job_scraper.py
import requests

def scrape_remoteok_jobs(query, max_results=50):
    url = "https://remoteok.com/api"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        jobs_data = response.json()
    except Exception as e:
        print(f"Failed to fetch data from RemoteOK: {e}")
        return []

    jobs = []
    query_lower = query.lower()

    for job in jobs_data[1:]:  # Skip metadata row at index 0
        position = job.get("position", "")
        company = job.get("company", "")
        description = job.get("description", "")
        tags = " ".join(job.get("tags", []))
        link = job.get("url", "")

        full_text = f"{position} {tags} {description}".lower()
        if query_lower in full_text:
            jobs.append({
                "title": position,
                "company": company,
                "description": description,
                "link": link
            })
            if len(jobs) >= max_results:
                break

    return jobs
