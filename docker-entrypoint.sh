#!/bin/bash

# Collect static files
echo "Collecting static files"
python3 manage.py collectstatic -l --noinput

# Apply database migrations
echo "Applying database migrations"
python3 manage.py migrate

# Add cron job schedules
python3 manage.py crontab add

# Start application
apache2ctl -D FOREGROUND
