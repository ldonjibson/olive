release: python manage.py migrate
web: gunicorn olive_app.wsgi --log-file - --log-level debug