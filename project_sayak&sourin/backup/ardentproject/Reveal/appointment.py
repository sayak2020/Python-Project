#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
n=form['name'].value
p=form['phone'].value
e=form['email'].value
a=form['age'].value
g=form['gender'].value
bg=form['bg'].value
dob=form['birthday'].value
pin=form['pincode'].value
sl=''
st='p'
cur.execute("insert into appointment values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')".format(sl,n,p,e,a,g,bg,dob,pin,st))
db.commit()
print("""
<html>

<head>
  <meta charset="utf-8">
  <title>BloodFair</title>
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <meta content="" name="keywords">
  <meta content="" name="description">

  <!-- Favicons -->
  <link href="img/favicon.png" rel="icon">
  <link href="img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,700,700i|Raleway:300,400,500,700,800|Montserrat:300,400,700" rel="stylesheet">

  <!-- Bootstrap CSS File -->
  <link href="lib/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Libraries CSS Files -->
  <link href="lib/font-awesome/css/font-awesome.min.css" rel="stylesheet">
  <link href="lib/animate/animate.min.css" rel="stylesheet">
  <link href="lib/ionicons/css/ionicons.min.css" rel="stylesheet">
  <link href="lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">
  <link href="lib/magnific-popup/magnific-popup.css" rel="stylesheet">
  <link href="lib/ionicons/css/ionicons.min.css" rel="stylesheet">

  <!-- Main Stylesheet File -->
  <link href="css/style.css" rel="stylesheet">

  <!-- =======================================================
    Theme Name: Reveal
    Theme URL: https://bootstrapmade.com/reveal-bootstrap-corporate-template/
    Author: BootstrapMade.com
    License: https://bootstrapmade.com/license/
  ======================================================= -->
</head>
<section id="intro">
    <div class="container">
        <div class="section-header">
          <h2>Your request was a success!!</h2>
          <p>We will Reach in 24 hrs.</p>
        </div>
    </div>    

    <div class="intro-content">
      <h2><span>Congrats! Get ready to recive a call withing 24 hr</span><br></h2>
      <div>
        <a href="user.html" class="btn-get-started scrollto">Back to user</a>
        <a href="appointment.html" class="btn-projects scrollto">Make another appintment</a>
      </div>
    </div>

    

  </section><!-- #intro -->


<html>""")
