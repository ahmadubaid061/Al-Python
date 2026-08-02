from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def input():
    return render_template('index.html')


@app.route('/submit',methods=['POST'])
def submit():
    first_name=request.form['first-name']
    last_name=request.form['last-name']
    return f'Hello {first_name} {last_name}'
    

if __name__=='__main__':
    app.run(debug=True)