#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
n=form['name'].value
e=form['email'].value
p=form['password'].value
ph=form['phone'].value
sl=''
if len(n)==0 or len(e)==0 or len(p)==0 or len(ph)==0 :
    print('No data given')
cur.execute("SELECT email FROM register ")
x=cur.fetchall()
print()
c=0
for i in x:
   if i[0]==e:
    c=1
    break
if c==0:    
    cur.execute("insert into register values('{0}','{1}','{2}','{3}','{4}')".format(sl,e,p,n,ph))
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
  background-color: #29CD3A;
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
<meta http-equiv = "refresh" content="5; URL=http://localhost/ardentproject/Reveal/login.html" />
        
</head>
        
 <body>

<br><h2 align="center">CONGRATULATIONS</h2>

<h4 align="center">Redirecting to Login Page within 5 seconds...<h4>
<div class="alert">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
  <p align="center"><strong>Registered Successfully!</strong></p>
</div>

</body>

        </html>""")
else :
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
<meta http-equiv = "refresh" content="5; URL=http://localhost/ardentproject/Reveal/register.html" />

</head>

<body>

<br><h2 align="center">Alert !</h2>

<h4 align="center">Redirecting to Registration Page within 5 seconds...</h4>
<div class="alert">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
  <p><strong>Error!</strong> Email ID Already Exists ! Try with different Email ID !<p>
</div>

</body>
 </html>""")
 

