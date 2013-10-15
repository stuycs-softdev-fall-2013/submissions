from flask import Flask, request, render_template, redirect, session, url_for
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('data.db')

@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/about")
def about():
    return "<h1>About</h1>"

@app.route("/hidden")
def hidden():
    if 'username' in session:
        return "<h1> in the secret page </h1>"
    else:
        return redirect(url_for('login'))

@app.route("/login", methods = ['GET', 'POST'])
def login():
	data = conn.cursor()
    if request.method=="GET":
		return render_template("login.html", message = "")
    else:
		name = request.form['username']
		pw = request.form['password']
		for data.execute('select * from account'):
			if user == name && pass = pw:
			session['username'] = name
			redirect(url_for('hidden.html'))
		else:
			return render_template("login.html", message = "Invalid Username or Password")
	data.close()

@app.route("/register", methods = ['GET', 'POST'])
def register():
	data = conn.cursor()
	if request.method=="GET":
		return render_template("register.html")
	else:
		name = request.form['username']
		pw = request.form['password']
		for user in data.execute('select * from account'):
			if user is None:
				data.execute('INSERT INTO account VALUES (name,pw)')
				data.commit()
				return redirect(url_for('about'))
			else:
				return render_template("register.html", message = "Username Taken")
	data.close()

@app.route("/logout")
def logout():
	session.pop('count', None)
	return render_template("login.html", message = "Welcome!")

if __name__=="__main__":
    app.debug=True
    app.run()
