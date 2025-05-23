# jobmatcher/src/job_scraper_factory.py

from src.job_scraper import scrape_remoteok_jobs
# from src.adzuna_scraper import scrape_adzuna_jobs
from src.wellfound_scraper import scrape_wellfound_jobs
from src.lever_scraper import scrape_lever_jobs

def get_scraper(source):
    source = source.lower()

    if source == 'remoteok':
        return scrape_remoteok_jobs
    # elif source == 'adzuna':
    #     return scrape_adzuna_jobs
    elif source == 'wellfound':
        return scrape_wellfound_jobs
    elif source == 'lever':
        return lambda query: scrape_lever_jobs(company="figma", query=query)

    raise ValueError(f"Unsupported job source: {source}")
