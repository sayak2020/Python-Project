#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
e=form['email'].value
cur.execute("SELECT * FROM appointment where status='d' and email='{0}'".format(e) )
x=cur.fetchall()
db.commit()
print("""
		<html>
		<head>
		<meta charset="UTF-8">
		 <title>Customers</title>
         <h2>Previous Appointments</h2>
         
         
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
		<th>name</th>
		<th>phone</th>
        <th>email</th>
        <th>age</th>
        <th>gender</th>
        <th>Daate Of appointment</th>
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
        <td>{5}</td>
        <td>{6}</td>
        </tr>
		
		
		
	""".format(x[i][0],x[i][1],x[i][2],x[i][3],x[i][4],x[i][5],x[i][7]))
    
print("""
		</tbody>
        </table>
		
		</body>
		</html>
	""")
