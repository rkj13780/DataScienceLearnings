from flask import Flask, render_template, request
from db import Database

app = Flask(__name__)
dbo =Database()
@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')
    

    #return name + " " + email + " " + password;
    registration = dbo.insert(name, email, password)
    #return registration
    if(registration):
        return render_template('login.html',message="Registration successful, kindly login!")
    else:
        return render_template('register.html',message="Email already exists. Registration Failed") 
    

@app.route('/perform_login', methods=['POST'])
def perfrom_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')
    result= dbo.search(email,password)
    if result :
        return "Welcome to the sytem"
    else: 
        return "Incorrect email/password"
    


app.run(debug=True)