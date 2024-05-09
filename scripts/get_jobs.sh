echo "start get_jobs.sh"

cd /app
# scrape indeed
/usr/local/bin/python -m crons.cron_indeed

# delete old records
/usr/local/bin/python -m crons.clean

echo "finish get_jobs.sh"
