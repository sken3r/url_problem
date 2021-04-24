install-dependencies:
	pip install poetry
	# alternatively: curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
	poetry --version
	poetry config virtualenvs.in-project true
	poetry install -vv

lint:
	isort -m 3 --tc --skip-glob **/*.pyi --skip-glob **pb2**.py url_shortener/
	black url_shortener/ --line-length 100
	flake8 --max-complexity=10 --ignore=E501 url_shortener/
	git diff --exit-code --