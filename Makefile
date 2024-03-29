python3=python3

clean-build:
	rm -rf pyworking_cz/build

check: venv/packages-installed
	venv/bin/pytest -v tests

flask-run: venv/packages-installed
	FLASK_APP=pyworking_cz FLASK_DEBUG=1 venv/bin/flask run

freeze: clean-build venv/packages-installed
	venv/bin/python freeze.py

venv: venv/packages-installed

venv/packages-installed: setup.py
	test -d venv || $(python3) -m venv venv
	venv/bin/pip install -U pip wheel
	venv/bin/pip install -e .[test]
	touch $@

docker-run:
	docker build --tag pyworking_cz .
	docker run --rm -it -p 8000:8000 pyworking_cz
