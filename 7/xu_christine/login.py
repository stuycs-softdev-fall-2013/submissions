#Submitted by Christine  and Glib 

from flask import Flask
from flask import session,url_for,request,redirect,render_template

app = Flask(__name__)


@app.route("/")
def home():
 if 'username' in session:        
        page = """
        <h1> This is the main page for %s</h1>
        <a href="/logout">Logout</a>
        """
        return page%(session['username'])
                  
   else:
	return "<h1> This is the Main Page. Welcome Everyone!!</h1>"
	
<style type="text/css">
.my_content_container a {
    border-bottom: 1px solid #777777;
    border-left: 1px solid #000000;
    border-right: 1px solid #333333;
    border-top: 1px solid #000000;
    color: #000000;
    display: block;
    height: 2.5em;
    padding: 0 1em;
    width: 5em;       
    text-decoration: none;       
}
// :hover and :active styles left as an exercise for the reader.
</style>

<div class="my_content_container">
    <a href="/login">Go to my link location</a>
</div>



@app.route("/login")
def login():
    "<h1> This is the login page </h1>"
    "<h1> Please enter your login information. </h1>"

<form method = "POST">

Username: <input type="text" name="username" value=""><br>
Password: <input type="password" name="password" value=""><br>

<input type="submit" name="button" value="Register">

</form>

@app.route('/register', methods=['GET','POST'])
def register():
  if request.method == 'POST':
<<<<<<< HEAD
    #Add to database
  return render_template('register.html')
  

@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('home'))

=======
  return render_template('register.html')
  
>>>>>>> 9c89bbe51f7ff595964946b741dc6d532bd19aac

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)

