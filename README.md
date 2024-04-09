# VisaHack Scraper
Scraper for VisaHack project.

## Running the cron
running the indeed cron, run this:
```
python -m crons.cron_indeed
```

## Build Docker image
docker build --target production -t ghcr.io/karintomania/visahack_scrape:latest .
docker push ghcr.io/karintomania/visahack_scrape:latest 
docker inspect ghcr.io/karintomania/visahack_scrape:latest 
