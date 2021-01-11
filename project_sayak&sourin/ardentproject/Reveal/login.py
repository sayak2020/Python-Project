#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
e=form['email'].value
p=form['password'].value
cur.execute("SELECT email FROM register ")
x=cur.fetchall()
c=0
for i in x:
   if i[0]==e:
    c=1
    break
if c==1:
    cur.execute("select password from register where email='{0}'".format(e))
    password=cur.fetchone()
    db.commit()
    if password[0]==p:
        print("""
        <html>
        <head>
        <script>document.cookie = "emailg = {0};";</script>
        
        
        <meta http-equiv = "refresh" content="0; URL=http://localhost/ardentproject/Reveal/user.html" />
        </head>
        </html>""".format(e))
        
    else :
        print("""
        <html>
        <head>
        <style>
    div { 
margin: 0 auto; 
width:1000px;
}
    
.alert {
  padding: 30px;
  background-color: #f44336;
  color: white;
}

.closebtn {
  margin-left: 15px;
  color: white;
  font-weight: bold;
  float: right;
  font-size: 22px;
  line-height: 20px;
  cursor: pointer;
  transition: 0.3s;
}

.closebtn:hover {
  color: black;
}

h2 {
  font-size: 25px;
}

h4 {
  font-size: 21px;
}

p {
  font-size: 25px;
}

</style>

        <meta http-equiv = "refresh" content="4; URL=http://localhost/ardentproject/Reveal/login.html" />
        </head>
        
        <body>

<br><h2 align="center">Login Failed !</h2>

<h4 align="center">Redirecting to Login Page within 4 seconds...<h4>
<div class="alert">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
  <p align="center"><strong>Login Failed! Try Entering Correct Password</strong></p>
</div>

</body>
        
        </html>""")
else:
    db.commit()
    print("""
    <html>
    <head>
    <style>
    div { 
margin: 0 auto; 
width:1000px;
}
    
.alert {
  padding: 30px;
  background-color: #f44336;
  color: white;
}

.closebtn {
  margin-left: 15px;
  color: white;
  font-weight: bold;
  float: right;
  font-size: 22px;
  line-height: 20px;
  cursor: pointer;
  transition: 0.3s;
}

.closebtn:hover {
  color: black;
}

h2 {
  font-size: 25px;
}

h4 {
  font-size: 21px;
}

p {
  font-size: 25px;
}

</style>
    
    <meta http-equiv = "refresh" content="4; URL=http://localhost/ardentproject/Reveal/register.html" />
    </head>
    
    <body>

<br><h2 align="center">NO USER FOUND !</h2>

<h4 align="center">Redirecting to Registration Page within 4 seconds...<h4>
<div class="alert">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
  <p align="center"><strong>YOU ARE NOT REGISTERED !</strong></p>
</div>

</body>
    
    
    </html>""")