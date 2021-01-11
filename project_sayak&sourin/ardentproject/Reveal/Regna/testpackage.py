#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
e=form['email'].value
t=form['package'].value
sl=''
s="p"
rep=""
r1=""
r2=""
r3=""
r4=""
cur.execute("insert into test values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(sl,e,t,s,r1,r2,r3,r4))
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
        
        <meta http-equiv = "refresh" content="4; URL=http://localhost/ardentproject/Reveal/user.html" />
        </head>
        
        <body>

<br><h2 align="center">CONGRATULATIONS</h2>

<h4 align="center">Redirecting to User Panel within 4 seconds...<h4>
<div class="alert">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
  <p align="center"><strong>TEST Booked Successfully!</strong></p>
</div>

</body>
        
        </html>""")
