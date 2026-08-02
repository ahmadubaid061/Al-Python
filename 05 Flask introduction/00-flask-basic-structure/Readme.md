# Flask Basics

A single-file example to understand what Flask is and how routes work.

## What is Flask?

Flask is a lightweight Python web framework. It lets you turn Python functions into web pages by mapping URLs to functions.

## Installing Flask

```bash
pip install flask
```

## Importing Flask

```python
from flask import Flask

app = Flask(__name__)
```

- `Flask(__name__)` creates the app object. `__name__` tells Flask where the file is located, so it knows where to look for things like templates and static files.

## Defining Routes

A route connects a URL to a Python function.

```python
@app.route('/')
def home():
    return 'Hello from flask!'
```

- `@app.route('/')` says "when someone visits this URL, run the function below it."
- Whatever the function returns is sent to the browser as the response.

In this file there are three routes:

- `/` → returns a plain text greeting
- `/about` → returns a short text message
- `/contact` → returns actual HTML (headings, line breaks, paragraphs) written directly as a string

## Returning HTML Directly

```python
@app.route('/contact')
def contact():
    return '<h2>Contact Info</h2> ...'
```

You can return HTML as a plain string, and the browser will render it like a normal webpage. This works fine for small examples, but for real projects you'd use `render_template()` with separate `.html` files instead (see the Jinja2 example).

## Running the App

```bash
python app.py
```

Then visit `http://127.0.0.1:5000/`, `/about`, or `/contact` in your browser.
