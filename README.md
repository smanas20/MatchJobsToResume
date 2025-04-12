# JobMatcher: AI-Powered Job Search Automation

This project automates job searching by:
- Scraping job boards (currently RemoteOK, with Adzuna and Wellfound support planned)
- Matching job listings against your resume using NLP
- Exporting results to both a CSV and a Google Sheet

## Features
- ✅ Resume matching using TF-IDF and cosine similarity
- ✅ Live scraping from RemoteOK
- ✅ Google Sheets export via service account
- 🔜 Support for Adzuna and Wellfound APIs
- 🔜 Filters for location, H1B sponsorship, tags, and salary

## Setup

1. **Clone the repo & create a virtual environment**
```bash
git clone https://github.com/yourusername/MatchJobsToResume.git
cd jobmatcher
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Prepare your resume**
- Save your resume as plain text: `data/resume.txt`

3. **Set up Google Sheets export**
- Create a [Google service account](https://console.cloud.google.com/)
- Enable Sheets and Drive API
- Download `credentials.json` and place it in the project root
- Share your Google Sheet with the service account email

4. **Run the project**
```bash
python main.py
```

## Configuration

You can change the job board and filters in `main.py`:
```python
job_source = 'remoteok'  # options: remoteok, adzuna, wellfound
jobs = scraper(query="automation engineer")
```

## Security

Make sure to:
- Add `credentials.json` to your `.gitignore`
- Never commit secret API keys

## License

MIT License
