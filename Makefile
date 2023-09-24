migrate:
	from library.extension import db
	from library.model import Students
	db.create_all()

init:
	python3 -m venv myenv && source myenv/bin/activate

app:
	pip install Flask==2.0
	pip freeze > requirements.txt

dep:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt
	pip freeze

run:
	flask run --debugger --reload
