#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
cur.execute("SELECT register.name,register.phone,test.email,test.test FROM test INNER join register ON test.email=register.email where test.status='p'")
x=cur.fetchall()
db.commit()
print("""
		<html>
		<head>
        
        <input type="button" class="button" value="&#8592; Back" onclick="window.location.href='admin.html'">
        
        <meta charset="UTF-8">
		 <title>Pending</title>
        <h2 align="center" class="sansserif">PENDING REPORTS</h2>
        <style>
        
        .sansserif {
  font-family: Arial, Helvetica, sans-serif;
}
        
        .button {
  background-color: #080794; /* Blue */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
        
        
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
</head>
<body>
		
		<table id="customers">
		<thead>
		<th>Name</th>
		<th>Phone</th>
        <th>Email</th>
        <th>Test</th>
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
        </tr>
		
		
		
	""".format(x[i][0],x[i][1],x[i][2],x[i][3]))
    
print("""
		</tbody>
        </table>
		
		</body>
		</html>
	""")
print("""
<html>
<style>

        
        form { 
margin: 0 auto; 
width:500px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

input[type=email] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}

input[type=text] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}
        
        
</style>        
<body>
<form action="admin_report_update.py" method="post"><br>
<h2 align="center">Publish Reports!</h2>
Enter Email ID: <input type="email" name="email" required><br>
Enter Test Name: <input type="text" name="test_name" required><br>
<h4>Enter Report</h4><br> 
<input type="text" name="r1" required placeholder=line1><br>
<input type="text" name="r2" required placeholder=line2><br>
<input type="text" name="r3" required placeholder=line3><br>
<input type="text" name="r4" required placeholder=Remarks><br>
<br/><button type="submit" value="update" >UPDATE</button>

</form>
</body>
</html>
""")