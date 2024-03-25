FROM  python:3.10

WORKDIR /app

# Install Python dependencies from requirements.txt
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install cron, wget for downloading, and software-properties-common for add-apt-repository
RUN apt-get update && apt-get install -y cron chromium chromium-driver 
 
COPY crontab /etc/cron.daily/crontab

RUN chmod 644 /etc/cron.daily/crontab
RUN crontab /etc/cron.daily/crontab
RUN mkdir /app/logs/
RUN touch /app/logs/cron.log

CMD  cron && tail -f /app/logs/myapp.log
