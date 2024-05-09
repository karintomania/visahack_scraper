echo "start expiraiton_check.sh"

cd /app
# scrape indeed
/usr/local/bin/python -m crons.expiration_check

echo "finish expiraiton_check.sh"
