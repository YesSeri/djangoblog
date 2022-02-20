# My Blog

## Deploy

`gunicorn mysite.wsgi:application --bind 0.0.0.0:3000`
use `--daemon` to run in background.