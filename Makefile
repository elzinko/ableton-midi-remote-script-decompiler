.PHONY: test

test:
	python -m unittest discover

lint:
	pylint --rcfile=.pylintrc *.py
