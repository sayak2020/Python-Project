#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
a=int(form['age'].value)
z=form['z'].value
s=form['s'].value
p=form['p'].value
status=''
sl=''
if a<10 or a>65:
    if z=='red' or z=='orange':
        status='mr'
        if p=='yes':
            status='hr'
    else:
        status='mr'
else:
    if z=='green':
        status='lr'
        if p=='yes':
            status='hr'
    else:
        status='mr'
        if p=='yes':
            status='hr'
cur.execute("insert into riskanalysis values('{0}','{1}')".format(sl,status))
db.commit()
if status=='lr':
    print("""
<html>
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

p {
  font-size: 25px;
}

</style>
<body>
<div class="alert">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
  <p align="center"><strong>You are in Low Risk</strong></p>
</div>
</body>
<html>""")
elif status=='mr':
    print("""
<html>
<style>
    div { 
margin: 0 auto; 
width:1000px;
}
    
.alert {
  padding: 30px;
  background-color: #F2950F;
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

p {
  font-size: 25px;
}

</style>
<body>
<div class="alert">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
  <p align="center"><strong>You are in Moderate Risk</strong></p>
</div>
</body>
<html>""")
else:
    print("""
<html>
<style>
    div { 
margin: 0 auto; 
width:1000px;
}
    
.alert {
  padding: 30px;
  background-color: #F2370F;
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

p {
  font-size: 25px;
}

</style>
<body>
<div class="alert">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
  <p align="center"><strong>CAUTION ! You are under High Risk</strong></p>
</div>
</body>
<html>""")

print("""
<html>
<style>

.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}

    

p {
  font-size: 25px;
}
</style>

<body>
<h1 align="center">Overall Statistics</h1><br>
<img src='plot/risk_analysis.png' width='1000' height='600' class="center">
</body>
<html>""")
            