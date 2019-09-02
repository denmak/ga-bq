gcloud config set project denmak-clickstream
pause
gcloud app deploy queue.yaml
gcloud app deploy cron.yaml
gcloud app deploy
pause
gcloud app browse