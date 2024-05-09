# Base stage for common setup
FROM  python:3.10 AS base

WORKDIR /app

# Install cron, wget for downloading, chromium and chromedriver
RUN apt-get update && apt-get install -y cron chromium chromium-driver

# Development stage
FROM base AS development
# Install Python dependencies from requirements.txt
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# No need to copy the application code, as it will be mounted via volumes in docker-compose.yml
CMD ["tail", "-f", "/dev/null"]

# Production stage
FROM base AS production
# Copy the application source code
COPY . /app

RUN pip install --no-cache-dir -r requirements-prod.txt

LABEL org.opencontainers.image.source=https://github.com/karintomania/visahack_scraper
RUN chmod +x /app/scripts/*.sh
