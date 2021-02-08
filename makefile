.PHONY: clean init

init: clean
	pipenv --python 3.7
	pipenv install --dev

lint: pylint flake8

flake8:
	pipenv run flake8 api/ --max-line-length=120 --exclude=test,database

pylint:
	pipenv run pylint --rcfile=setup.cfg api/

reformat: black isort

black:
	pipenv run black api/endpoints/
	pipenv run black api/tests/

isort:
	pipenv run isort api/*.py
	pipenv run isort api/endpoints/**/*.py

ci-bundle: reformat lint test

test:
	pipenv run pytest -vv --cov-report=term-missing --cov=api/endpoints api/tests

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -rf .hypothesis
	rm -rf .pytest_cache
	rm -rf .tox
	rm -f report.xml
	rm -f coverage.xml
