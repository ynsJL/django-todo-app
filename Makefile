# Local Setup
setup:
	python -m venv .venv
	python manage.py migrate
	pip install -r requirements.txt

# Create super user
super-user:
	python manage.py createsuperuser

# Run the project
run:
	python manage.py runserver

# Run Test
test:
	python manage.py test myapp.tests -v 2

# Run Test Coverage
test-coverage:
	coverage run --source='.' manage.py test myapp
	coverage report -m
	coverage html
	coverage xml
	coverage-badge -f -o coverage.svg