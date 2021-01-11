#!C:\Users\sayak\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
import cgi
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
form=cgi.FieldStorage()
e=form['email'].value
print(e)
print("""
   <html lang="en">
<title>BloodFair</title>
<head>
  <meta charset="utf-8">
  
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
<!--==========================
      TESTS OFFERED
    ============================-->
    <section id="services">
      <div class="container">
        <div class="section-header">
          <h2>User Panel</h2>
          <p> Hello User , Welcome to user panel. Check out various options below and click on any option to access.</p>
        </div>

        <div class="row">

          <div class="col-lg-10">
            <div class="box wow fadeInLeft">
              <div class="icon"><i class="fa fa-heartbeat"></i></div>
              <h4 class="title"><a href="appointment.html?e=$_POST(email)">Book an Appointment with us     ►</a></h4>
              <p class="description">Quicky book an Appointment by filling up some details</p>
            </div>
          </div>

          <div class="col-lg-10">
            <div class="box wow fadeInRight">
              <div class="icon"><i class="fa fa-tint"></i></div>
              <h4 class="title"><a href="Regna\testpackage.html">Tests Offered     ►</a></h4>
              <p class="description">We provide accurate and precise diagnostic, prognostic and predictive testing services in a timely manner</p>
            </div>
          </div>

          <div class="col-lg-10">
            <div class="box wow fadeInLeft" data-wow-delay="0.2s">
              <div class="icon"><i class="fa fa-asl-interpreting"></i></div>
              <h4 class="title"><a href="">View Reports     ►</a></h4>
              <p class="description">Check the reports of your previous tests</p>
            </div>
          </div>


        </div>

      </div>
    </section><!-- #services -->
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
print('hi2')