install:
	virtualenv venv
	. venv/bin/activate
	pip install -r requirements.txt

waitress:
	waitress-serve app:app

flask:
	FLASK_APP=app flask run --debug

build:
	buildah build .
