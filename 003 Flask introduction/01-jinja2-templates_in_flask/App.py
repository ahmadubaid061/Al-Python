from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',name='Ubaid')

@app.route('/base')
def base():
    return render_template('base.html',name="Ubaid")

@app.route('/about')
def about():
    return render_template('about.html',name="Ubaid")

if __name__=='__main__':
    app.run(debug=True, use_reloader=False)