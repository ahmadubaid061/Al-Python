from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def input():
    return render_template('index.html')


@app.route('/submit',methods=['POST'])
def submit():
    first_name=request.form['first-name'] #request.form.get("user-name)
    last_name=request.form['last-name']
    return f'Hello {first_name} {last_name}'
'''
note! request.form['first-name'] will return an error if username is nul
but if you want to ignore null and use a safe method then you can use
request.form.get("user-name)
'''

    

if __name__=='__main__':
    app.run(debug=True)