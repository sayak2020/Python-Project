#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
i=int(form['index'].value)
i=i-1
email=form['e'].value
cur.execute("SELECT register.name,register.phone,test.email,test.test FROM test INNER join register ON test.email=register.email and test.email='{0}'where test.status='d'".format(email))
x=cur.fetchall()
test=x[i][3]
cur.execute("SELECT register.name,register.phone,register.email,test.test,test.r1,test.r2,test.r3,test.r4 FROM test INNER join register ON test.email=register.email where test.status='d' and test.email='{0}' and test.test='{1}' ".format(email,test))
res=cur.fetchall()
db.commit()
print("""
        
<html lang="en">
<head>
 <meta charset="UTF-8">
 <title>Print report</title>
 <link rel="stylesheet" type="text/css" href="//cdnjs.cloudflare.com/ajax/libs/semantic-ui/1.12.0/semantic.min.css">
</head>
<body>
 <div class="ui page grid">
  <div class="wide column">
   <h1 class="ui header aligned center">BloodFair</h1>
   <div class="ui divider hidden"></div>
  </div>
 </div>
 <!-- scripts -->
 <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<script type="text/javascript" src="//cdn.rawgit.com/MrRio/jsPDF/master/dist/jspdf.min.js"></script> 






<div class="ui segment">
 <div class="ui button aligned center teal" id="create_pdf">PRINT REPORT</div>
 <form class="ui form" method="get" action="">
 <h1 class="ui header aligned center">BloodFair</h1>
 <p align="center"> We Care at BloodFair Labs</p>
 <div class="ui divider"></div>
 
  <h4 class="ui dividing header">Personal Information</h4>
   <div class="field">
    <label for="">Name</label>
    <input type="text" name="name" value="{0}" readonly>
   </div>
   <div class="field">
    <label for="">Phone</label>
    <input type="text" name="phone" value="{1}" readonly>
   </div>
   <div class="field">
   <label for="">email</label>
    <input type="text" name="email" value="{2}" readonly>
  </div>
  <div class="field">
   <label for="">Test Name</label>
    <input type="text" name="test" value="{3}" readonly>
  </div>
  <br><br>
  
  
  <h4 class="ui dividing header">REPORT</h4>
  <div class="field">
    <label for=""></label>
    <input type="text" name="l1" value="{4}" readonly>
   </div>
   <div class="field">
    <label for=""></label>
    <input type="text" name="l2" value="{5}" readonly>
   </div>
   <div class="field">
   <label for=""></label>
    <input type="text" name="l3" value="{6}" readonly>
  </div>
  <div class="field">
   <label for="">Remarks</label>
    <input type="text" name="l4" value="{7}" readonly>
  </div>
  <br><br>
  <h1 class="ui header aligned center">Tips From Expert</h1>
  <p>* Dont drink sugar calories</p>
  <p>* Take care of your gut health with probiotics and fiber</p>
  <p>* Dont overcook or burn your meat</p>
  <p>* Dont smoke or do drugs, and only drink in moderation if cant deny</p>
  <p>* TEST AFTER 3 MONTHS</p>
  </div>
  </form>
</div>






<script type="text/javascript" src="//cdn.rawgit.com/niklasvh/html2canvas/0.5.0-alpha2/dist/html2canvas.min.js"></script>
 <script type="text/javascript" src="app.js"></script>
</body>
""".format(res[0][0],res[0][1],res[0][2],res[0][3],res[0][4],res[0][5],res[0][6],res[0][7]))
print("</html>")