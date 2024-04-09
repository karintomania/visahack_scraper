echo "start entrypoint.sh"

cd /app
/usr/local/bin/python -m crons.cron_indeed

echo "finish entrypoint.sh"
