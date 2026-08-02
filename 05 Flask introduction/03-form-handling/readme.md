# Flask Form Handling Example

A simple Flask application demonstrating how to handle HTML form input using POST requests.

## How It Works

### 1. **floder Strucure**

```
root/
├── app.py              # Main Flask application
└── templates/
    └── index.html      # HTML form template
```

### 2. **The HTML Form** (`templates/index.html`)

- Uses `method="POST"` to send data securely
- Form `action="/submit"` points to the route that processes the data
- Each input has a `name` attribute (`first-name`, `last-name`) that Flask uses to access the data

### 3. **Flask Routes**

#### Route 1: Display Form (`/`)

```python
@app.route("/")
def input():
    return render_template('index.html')
```

- Renders and displays the HTML form when user visits the root URL

#### Route 2: Process Form Data (`/submit`)

```python
@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    return f'Hello {first_name} {last_name}'
```

- Only accepts POST requests
- Uses `request.form['field-name']` to retrieve form data
- Returns a personalized greeting

### 4. **Key Concepts**

| Concept             | Explanation                                                   |
| ------------------- | ------------------------------------------------------------- |
| `request.form`      | Dictionary containing form data submitted via POST            |
| `methods=['POST']`  | Restricts route to only accept POST requests                  |
| `name` attribute    | HTML input's `name` must match the key used in `request.form` |
| `render_template()` | Renders HTML templates from the `templates/` folder           |

### 5. **Running the Application**

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

## Why Use POST?

- **Security**: Data is not visible in the URL
- **No size limits**: Can handle large amounts of data
- **Data types**: Can send files and complex data

## Important Notes

- Always place templates in a `templates/` folder
- The `debug=True` enables auto-reload during development
- Form field names must match exactly between HTML and Flask code

---
