echo "start expiraiton_check.sh"

cd /app
# scrape indeed
/usr/local/bin/python -m crons.cron_expiration_check

echo "finish expiraiton_check.sh"
