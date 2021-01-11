#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
e=form['email'].value
cur.execute("SELECT register.name,register.phone,test.email,test.test FROM test INNER join register ON register.email=test.email and test.email='{0}' where status='d'".format(e))
x=cur.fetchall()
db.commit()
print("""
		<html>
		<head>
		<meta charset="UTF-8">
		 <title>pending Report</title>
         <h2>Your RESULTS</h2>
         
         <style>
#customers {
  font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #080794;
  color: white;
}
</style>
         
         
		<body>
		
		<table id="customers">
		<thead>
        <th>sl</th>
		<th>Name</th>
		<th>phone</th>
        <th>Email</th>
        <th>Test </th>
		</thead>
		<tbody>

""")
for i in range(len(x)):
    print("""
		
		<tr>
		<td>{0}</td>
		<td>{1}</td>
        <td>{2}</td>
        <td>{3}</td>
        <td>{4}</td>
		</tr>
		
		
		
	""".format(i+1,x[i][0],x[i][1],x[i][2],x[i][3]))
    
print("""
		</tbody>
        </table>
		
		</body>
		</html>
	""")
if not x:
    print("No Reports Yet")  
else:
    print("""
    <html>
    
    <body>
    <br><br>
    <h3>VIEW YOUR REPORT</h3>
    <form action="viewreport_user.py" method="post">
    Sl: <input type="number" name="index" required><br>
    Email: <input type="text" name="e" value={0} readonly><br><br>
    <input type="submit" value="view">
    </form>
    </body>
    </html>
    """.format(e))