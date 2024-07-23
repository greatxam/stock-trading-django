#!/bin/bash

if [ "$1" == cron ]; then
  # Copy ENV to cron shell
  env > /etc/environment

  # Add cron job schedules
  python3 manage.py crontab remove
  python3 manage.py crontab add
else
  # Collect static files
  echo "Collecting static files"
  python3 manage.py collectstatic -l --noinput

  # Apply database migrations
  echo "Applying database migrations"
  python3 manage.py migrate
fi

# Start application command (CMD)
exec "$@"
