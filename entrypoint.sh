echo "start entrypoint.sh"

cd /app
# scrape indeed
/usr/local/bin/python -m crons.cron_indeed

# delete old records
/usr/local/bin/python -m crons.clean

echo "finish entrypoint.sh"
