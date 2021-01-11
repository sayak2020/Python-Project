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
    print('you are in Low risk')
elif status=='mr':
    print('                           you are in MODERATE risk')
else:
    print('CAUTION!!! You are under HIGH RISK')
print('\n overall statistics')

print("""
<html>
<body>
<h1>OVERALL STATISTICS:<h1><br/>
<img src='plot/risk_analysis.png' width='500' height='300'>
</body>
<html>""")
            