#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
n=form['name'].value
e=form['email'].value
s=form['subject'].value
m=form['message'].value
sl=''
cur.execute("insert into msg values('{0}','{1}','{2}','{3}','{4}')".format(sl,n,e,s,m))
db.commit()
print("Your message sent successfully!!!")
