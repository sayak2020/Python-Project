#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
e=form['email'].value
t=form['test_name'].value
r1=form['r1'].value
r2=form['r2'].value
r3=form['r3'].value
r4=form['r4'].value
cur.execute("UPDATE test SET status = 'd',r1='{0}',r2='{1}',r3='{2}',r4='{3}' WHERE email='{4}' and test='{5}'".format(r1,r2,r3,r4,e,t) )
db.commit()
print('updated')
print("""
        <html>
        <head>
        <meta http-equiv = "refresh" content="2; URL=http://localhost/ardentproject/Reveal/Regna/admin_report_fetch.py" />
        </head>
        </html>""")