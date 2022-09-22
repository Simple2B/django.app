# Creating environment

```
git init
git clone https://github.com/Simple2B/django.app.git
cd django.app
poetry install
cp sample.env .env
```

# Launch an run application locally

```
source .venv/bin/activate
python manage.py migrate
python manage.py runserver
```

# Run docker

```
docker compose up app
```
