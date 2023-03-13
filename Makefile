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

# for linux
admin3:
	./manage.py createsuperuser

app3:
	./manage.py startapp app

migrate3:
	./manage.py makemigrations
	./manage.py migrate

run3:
	./manage.py runserver

static3:
	./manage.py collectstatic

freeze3:
	pip freeze >requirements.txt
