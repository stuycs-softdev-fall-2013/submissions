from flask import Flask
from flask import session,url_for,request,redirect,render_template
from flask.ext import shelve

app = Flask(__name__)
app.config['SHELVE_FILENAME'] = 'login.db'
shelve.init_app(app)
app.secret_key="my supersecret key"
#breakline~~~~~~~~~~homecode~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/")
def home():
    #redirects to the login page
    return redirect("/login")
#breakline~~~~~~~~~~logincode~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/login", methods=['GET','POST'])
def login():
    #coding how the login page will look
    page ="""<h1>It's the Login Page FOOL!</h1>
        <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" name="button" value="login">
        <input type="submit" name="button" value="reset"><br><br><br><br><br><br><br>
        I pity the fool that don't have an account!<br>
        <input type ="submit" name="button" value="sign up">
        <br><br><br><br><br><br><br><br>
        <h6>Website by Mr T</h6>
        </form>"""
    if request.method == "GET":
        return page
    else:
        button = request.form['button']
        if button=="login":
            submitpage = "<h1>submitted fool!</h1>"
            username = request.form['username']
            password = request.form['password']
            submitpage = submitpage + username + " " + password
            return submitpage
        elif button=="reset":
            return redirect ("/login")
        else:
            return redirect ("/register")
#breakline~~~~~~~~~~logoutcode~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/logout")
def logout():
    return "<h1> swag </h1>"
#breakline~~~~~~~~~~registercode~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
@app.route("/register", methods=['GET','POST'])
def register():
    page="""<h1>Signup page's here fool!</h1>
        <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" name="button" value="sign up">
        <input type="submit" name="button" value="reset"><br><br><br><br><br><br>
        Fool already got a account? Get back in the game!<br>
        <input type ="submit" name="button" value="sign in">
        </form>
        """
    if request.method == "GET":
        return page
    else:
        button = request.form['button']
        if button=="sign up":
            submitpage = "<h1>signed up fool!</h1>"
            username = request.form['username']
            password = request.form['password']
            submitpage = submitpage + username + " " + password
            return submitpage
        elif button=="reset":
            return redirect ("/register")
        else:
            return redirect ("/login")
#breakline~~~~~~~~~~madlib~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("
#breakline~~~~~~~~~~count~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
if __name__ =="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=1337)
