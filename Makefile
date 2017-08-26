python3=python3

flask-run: venv/packages-installed
	env \
		PYTHONDONTWRITEBYTECODE=1 \
		FLASK_APP=pyworking_web.py \
		FLASK_DEBUG=1 \
		venv/bin/flask run

venv/packages-installed: requirements.txt
	test -d venv || $(python3) -m venv venv
	venv/bin/pip install -U pip wheel
	venv/bin/pip install -r requirements.txt
	touch $@

docker-run:
	docker build --tag pyworking-web .
	docker run --rm -it -p 8000:8000 pyworking-web
