#!/usr/bin/python
#!flask/bin/python

#This is Jack Cahn and Alvin Leung's Project

from flask import Flask
from flask import request
from flask import url_for,render_template
from flask import session,request,redirect
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'my_users.db'
app.secret_key="secret_key"
shelve.init_app(app)

@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/about")
def about():
    return "<h1>About</h1>"

@app.route("/login",methods=['GET', 'POST'])
def login():
    if request.method=="GET":
        my_users =  shelve.get_shelve('c')
        return render_template("login.html")
    else:
        button=request.form['button']
        if button=="login":
            username = request.form['username'].encode ('ascii',"ignore")
            password = request.form['password'].encode ('ascii',"ignore")
            if username in my_users and my_users [username]["password"] == password:
                session['username'] = username
                return redirect("/")
            else:
                return redirect ("/login")
        else:
            return redirect("/form")
                
@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=="GET":
        return render_template("form.html")
        d={'name':request.form['username'],
           'HR':request.form['HR']}
        button=request.form['button']
        if button=="Submit":
            s="%(name)s:%(HR)s\n"%(d)
            return redirect("/")
            return render_template("render_template.html",d=d)
        else:
            return redirect("/")


if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5005)
