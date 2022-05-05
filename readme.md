# Trello API: Project setup

## Create virtual environment

- virtualenv -p python3.8 venv

## Clone the repo:

- https://github.com/ingefull-git/trello_api.git

## Install requirements

- pip install -r requirements.txt

## Run dev-server

- python mange.py runserver

# Create cards:
## Make a POST request to:

If you want to add a TASK card run the commnad and will be added to the TASK list in the BOARD and create a LABEL with the category, in case somethin happend with the label, the card will be removed. 

- curl -X POST "http://127.0.0.1:8000/api/v1/" -H "Content-Type: application/json" -d '{"type":"task", "title":"Is a task", "category":"cat1"}' 

To add an ISSUE card:

- curl -X POST "http://127.0.0.1:8000/api/v1/" -H "Content-Type: application/json" -d '{"type":"issue", "title":"Is an issue", "description":"description of the issue"}'

To add a BUG card:

- curl -X POST "http://127.0.0.1:8000/api/v1/" -H "Content-Type: application/json" -d '{"type":"bug", "description":"description of the bug"}'

# Tests
## Coverage report to html

- pytest --cov-report html --cov=core_app tests
- copy the path of the index.html that is inside the htmlcov folder

## Run tests

- pytest -sv

