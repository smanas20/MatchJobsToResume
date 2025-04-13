from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_wellfound_jobs(query, location="remote", max_results=30):
    jobs = []
    url = f"https://wellfound.com/jobs?keywords={query.replace(' ', '%20')}&location={location.replace(' ', '%20')}"

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize ChromeDriver with options and service
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(5)  # Wait for JS to load

    # job_cards = driver.find_elements(By.CSS_SELECTOR, "div.styles_component__aS2pP")
    job_cards = driver.find_elements(By.CSS_SELECTOR, "div[data-test='JobCard']")


    for card in job_cards:
        try:
            # title = card.find_element(By.CSS_SELECTOR, "div.styles_title__xxx span").text
            # company = card.find_element(By.CSS_SELECTOR, "div.styles_subtitle__abc span").text
            # link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
            title = card.find_element(By.CSS_SELECTOR, "h3").text
            company = card.find_element(By.CSS_SELECTOR, "h2").text
            link = card.find_element(By.CSS_SELECTOR, "a").get_attribute("href")


            description = f"{title} at {company}"
            jobs.append({
                "title": title,
                "company": company,
                "description": description,
                "link": link
            })

            if len(jobs) >= max_results:
                break
        except Exception:
            continue

    driver.quit()
    return jobs
