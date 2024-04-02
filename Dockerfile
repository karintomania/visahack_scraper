# Base stage for common setup
FROM  python:3.10 AS base

WORKDIR /app

# Install Python dependencies from requirements.txt
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install cron, wget for downloading, chromium and chromedriver
RUN apt-get update && apt-get install -y cron chromium chromium-driver
 
# Applying cron job
COPY crontab /etc/cron.daily/crontab
RUN chmod 644 /etc/cron.daily/crontab \
    && crontab /etc/cron.daily/crontab \
    && mkdir /app/logs/ \
    && touch /app/logs/myapp.log

# Development stage
FROM base AS development
# No need to copy the application code, as it will be mounted via volumes in docker-compose.yml
CMD cron && tail -f /app/logs/myapp.log

# Production stage
FROM base AS production
# Copy the application source code
COPY . /app
COPY ./crontab-prod /etc/cron.daily/crontab

LABEL org.opencontainers.image.source=https://github.com/karintomania/visahack_scraper
CMD cron && tail -f /app/logs/myapp.log
