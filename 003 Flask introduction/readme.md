# Flask Introduction

A collection of small, self-contained Flask examples — each one builds on the last to introduce a new concept. Every subfolder has its own README with more detail.

## Structure

**`00-flask-basic-structure/`**
The starting point. A single file (`simple-flask-structure.py`) showing what Flask is, how to install it, and how to define basic routes that return plain text or raw HTML.

**`01-jinja2-templates_in_flask/`**
Introduces `render_template()` and the `templates/` folder. Covers passing variables into HTML with `{{ }}`, and template inheritance using `{% extends %}` and `{% block %}`.

**`03-form-handling/`**
Shows how to build an HTML form and handle its submission in Flask using `request.form`, including the difference between GET and POST requests.

## How to Explore

Go into each subfolder in order (00 → 01 → 03), read its `readme.md`, then run its Flask file:

```bash
cd 00-flask-basic-structure
python simple-flask-structure.py
```

Each example runs on `http://127.0.0.1:5000/` by default — open that in your browser after starting the file.

## Suggested Order

1. `00-flask-basic-structure` — routes and returning text/HTML
2. `01-jinja2-templates_in_flask` — templates and template inheritance
3. `03-form-handling` — forms and handling submitted data
