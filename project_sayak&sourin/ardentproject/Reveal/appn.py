#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
print('hi')
print("""
    <html>
<title> Appointment</title>
<head>
  <meta charset="utf-8">
  <title> Appointment</title>
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
<body>
<section id="clients" class="wow fadeInUp">
      <div class="container">
        <div class="section-header">
          <h2>Book An Appointment with us </h2>
          <p>We are here for you. Get ready to get a call back within 6 hours!</p>
        </div>

      </div>
    </section><!-- #clients -->

<form action="appointment.py" method="post" ><br><br>
 <div class="form-group col-md-9">
    Enter Name   : <input type="text" name="name" class="text-center""form-control" id="name" placeholder="Your Name" data-rule="minlen:4" required data-msg="Please enter at least 4 characters" />
    <br><br>
	<div class="validation"></div>
 </div>
 
 <div class="form-group col-md-9">
    Enter Phone No :  <input type="tel" name="phone" class="text-center""form-control" id="name" placeholder="Your Phone Number" pattern="[0-9]{10}" required data-msg="Enter a valid Phone Number" />
    <br><br>
	<div class="validation"></div>
 </div>
 
 <div class="form-group col-md-9">
    Enter Email Address :  <input type="email" name="email" class="text-center""form-control" id="name" placeholder="Your Email" data-rule="minlen:4" required data-msg="Please enter proper email" />
    <br><br>
	<div class="validation"></div>
 </div>
 
 <div class="form-group col-md-6">
    Enter Age : <input type="text" name="age" class="text-center""form-control" id="name" placeholder="Your Age" min="1" max="3" required data-msg="Please enter at least 4 chars" />
    <br><br>
	<div class="validation"></div>
 </div>
 
 <div class="form-group col-md-6">
    Select Gender  :  
  <input type="radio" class="text-center""form-control" id="male" name="gender" value="male" >
  <label for="male">Male </label>
  <input type="radio" class="text-center""form-control" id="female" name="gender" value="female">
  <label for="female">Female </label>
  <input type="radio" class="text-center""form-control" id="other" name="gender" value="other">
  <label for="other">Other </label>
    <br><br>
	<div class="validation"></div>
 </div>
 
 <div class="form-group col-md-6">
    Select Blood Group  :  
  <select name="cars" id="cars" >
    <option value="A+">A+</option>
    <option value="A-">A-</option>
    <option value="B+">B+</option>
    <option value="B-">B-</option>
	<option value="O+">O+</option>
    <option value="O-">O-</option>
    <option value="AB+">AB+</option>
    <option value="AB-">AB-</option>
  </select>
    <br><br>
	<div class="validation"></div>
 </div>
 
 <div class="form-group col-md-6">
    Date of Birth  :  
    <input type="date" id="birthday" name="birthday" required>
    <br><br>
	<div class="validation"></div>
 </div>
 
 <div class="form-group col-md-9">
    PIN Code :  <input type="tel" name="pincode" class="text-center""form-control" id="name" placeholder="Your PIN Code" pattern="[0-9]{6}" required data-msg="Enter a valid pin Number" />
    <br><br><br><br>
	<div class="validation"></div>
 </div>
 
 
<div class="text-center""text-center"><button type="submit">Take Appointment</button></div>
</form>
 <!-- JavaScript Libraries -->
  <script src="lib/jquery/jquery.min.js"></script>
  <script src="lib/jquery/jquery-migrate.min.js"></script>
  <script src="lib/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="lib/easing/easing.min.js"></script>
  <script src="lib/superfish/hoverIntent.js"></script>
  <script src="lib/superfish/superfish.min.js"></script>
  <script src="lib/wow/wow.min.js"></script>
  <script src="lib/owlcarousel/owl.carousel.min.js"></script>
  <script src="lib/magnific-popup/magnific-popup.min.js"></script>
  <script src="lib/sticky/sticky.js"></script>

  <!-- Contact Form JavaScript File -->
  <script src="contactform/contactform.js"></script>

  <!-- Template Main Javascript File -->
  <script src="js/main.js"></script>
</body>
</html>""")