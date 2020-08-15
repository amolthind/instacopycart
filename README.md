# Flask Project Template

This project template uses Flask and Flask-Bootstrap and comes with the following folder structure:

```
- templates/
  - index.html
  - base.html
  - another_page.html

- static/
  - css/
    - style.css
  - js/
    - script.js

- requirements.txt
- app.py
- Procfile
- README.md
```

## HTML Templates
HTML template files include:

* `base.html` which extends from `Bootstrap/base.html`
* `index.html` which extends from `base.html` and is served on the `('/')` route
* `another_page.html` which also extends from `base.html` and is served on the `('/anotherpage')` route

## Setup

1. Download the repo zip file locally (or use `git clone` with the HTTPS URL), extract it, and name the root folder your project name
2. Open the project folder with your code editor
3. Initialize Git with `git init`
4. Setup your Python virtual environment with: `python -m venv venv`
5. Activate your virtual environment with:
  * `venv/Scripts/activate` in Powershell
  * `source venv/bin/activate` in Terminal
6. Install the project template's Python dependencies with: `pip install -r requirements.txt`

## Run App
Run the app with `python app.py`. By default, the Flask server runs on `127.0.0.1:5000/`

A `Procfile` is also provided if you would like to deploy your app to a production grade server using **Heroku**. See https://devcenter.heroku.com/articles/getting-started-with-python#set-up