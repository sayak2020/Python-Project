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
print("TEST BOOKED SUCCESSFULLY")
print("""
        <html>
        <head>
        <meta http-equiv = "refresh" content="2; URL=http://localhost/ardentproject/Reveal/user.html" />
        </head>
        </html>""")
