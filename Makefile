install:
	python3 -m venv .venv
	.venv/bin/python3 --version
	.venv/bin/python3 -m pip install --upgrade pip
	.venv/bin/python3 -m pip install -r requirements.txt
