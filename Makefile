admin:
	python ./manage.py createsuperuser

app:
	python ./manage.py startapp app

migrate:
	python ./manage.py makemigrations
	python ./manage.py migrate

run:
	python ./manage.py runserver

static:
	python ./manage.py collectstatic

freeze:
	pip freeze >requirements.txt

