#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
s=int(form['sl'].value)
cur.execute("UPDATE appointment SET status = 'd' WHERE appointment.sl = {0}".format(s) )
db.commit()
print('updated')
print("""
        <html>
        <head>
        <meta http-equiv = "refresh" content="2; URL=http://localhost/ardentproject/Reveal/Regna/admin_appointment_fetch.py" />
        </head>
        </html>""")