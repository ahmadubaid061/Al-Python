from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return 'Hello from flask!'

@app.route('/about')
def about():
    return 'My Name is Ubaid and I am practicing flask'

# suppose i want to return some html to the browser
@app.route('/contact')
def contact():
    return '<h2>Contact Info</h2><br> <h3>Email : </h3> <p>ahmadubaidedu@gmail.com</p> <h3>Phone : </h3> <p>+923428994095 </P>'

if __name__== "__main__":
    app.run(debug=True,use_reloader=False)

    