#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
db.commit()
p=form['package'].value
print(p)
print("""
    <html>
    <head>
    <meta http-equiv = "refresh" content="5; URL=http://localhost/ardentproject/Reveal/package.html" />
    </head>
    </html>""")
