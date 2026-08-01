# Flask + Jinja2 Basics

A tiny Flask project to understand templates and template inheritance.

## Files

**`app.py`**
The main Flask application. It defines three routes:

- `/` → renders `home.html`
- `/base` → renders `base.html`
- `/about` → renders `about.html`

Each route calls `render_template()`, which loads an HTML file from the `templates/` folder and can pass variables (like `name`) into it.

**`home.html`**
A plain, standalone template. It uses `{{ name }}` to display a variable passed from `app.py`. This is a normal HTML page — it doesn't extend anything.

**`base.html`**
The "parent" template. It defines a `{% block content %}...{% endblock %}` section that child templates can override. Think of it as a reusable page layout (header, structure, etc.) that other pages build on top of.

**`about.html`**
A "child" template. It uses `{% extends "base.html" %}` to inherit everything from `base.html`, then overrides the `content` block to add its own content. `{{ super() }}` inside the block means "also keep whatever was in the parent's block."

## Key Concepts

- **`render_template('file.html', variable=value)`** — loads an HTML file and passes Python variables into it.
- **`{{ variable }}`** — Jinja2 syntax to print a variable's value in HTML.
- **`{% extends "base.html" %}`** — must be the very first line of a child template; it inherits the parent's layout.
- **`{% block name %} ... {% endblock %}`** — defines a section that a child template can override.
- **`{{ super() }}`** — inside a block, keeps the parent template's original content instead of replacing it.

## Running the App

```bash
python app.py
```

Then visit `http://127.0.0.1:5000/`, `/base`, or `/about` in your browser.
