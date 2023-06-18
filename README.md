# Python Flask MySQL Tutorials

## Setup project in Windows 10

### Install poetry

Poetry is package manager just like we have npm in NodeJS. Run bellow command to install poetry in windows 10 in powershell command prompt. Check [Poetry docs](https://python-poetry.org/docs/) for other platform installation.

```sh
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### Set poetry in path

We need to set executable path to access `poetry` command. Check [Stackoverflow solution](https://stackoverflow.com/a/75601518/11286367) to set path in command prompt.

```sh
$Env:Path += ";C:\Users\<username>\AppData\Roaming\Python\Scripts"; setx PATH "$Env:Path"
```

check poetry version

```sh
poetry --version
```

### Create new poetry project

```sh
poetry new <project-name>
```

### Install dependencies

It will setup and install poetry virtual environment.

```sh
poetry install
```

### Setup flask

```sh
poetry add flask
```

### Rename package name

rename `<your_project_name>` to `main` and add `app.py`

```py
"""Flask App main module"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'
```

## Run application

```sh
cd main
poetry run flask run
```

Just incase failed then try

```
poetry install
cd main
poetry run flask run
```

## Clean cache

```
poetry cache list
poetry cache clear <name> --all
```
