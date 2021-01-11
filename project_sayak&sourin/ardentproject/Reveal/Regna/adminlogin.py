#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
i=form['id'].value
p=form['password'].value
cur.execute("SELECT id FROM adminlogin ")
x=cur.fetchall()
c=0
for s in x:
   if s[0]==i:
    c=1
    break
if c==1:
    cur.execute("select password from adminlogin where id='{0}'".format(i))
    password=cur.fetchone()
    db.commit()
    if password[0]==p:
        print('login Successful')
        print("""
        <html>
        <head>
        <meta http-equiv = "refresh" content="0; URL=http://localhost/ardentproject/Reveal/Regna/admin.html" />
        </head>
        </html>""")
        
    else :
        print('Wrong password')
        print("""
        <html>
        <head>
        <meta http-equiv = "refresh" content="2; URL=http://localhost/ardentproject/Reveal/Regna/adminlogin.html" />
        </head>
        </html>""")
else:
    db.commit()
    print('Admin Id does not exist')
    print("""
    <html>
    <head>
    <meta http-equiv = "refresh" content="2; URL=http://localhost/ardentproject/Reveal/Regna/adminlogin.html" />
    </head>
    </html>""")
  