<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Bottle web project template">
    <meta name="author" content="datamate">
    <title>My UPI Project</title>
    <link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="/static/custom.css">
    <script type="text/javascript" src="/static/jquery.js"></script>
	<script type="text/javascript" src="/static/custom.js"></script>
    <script type="text/javascript" src="/static/bootstrap.min.js"></script> 
</head>
<body>

	
	  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
    <div class="container">
      <a class="navbar-brand" href="/">My UPI project</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <a class="nav-link" href="/">Početna
              <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item" id="about">
            <a class="nav-link" href="/about">O nama</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/tattoo">Tetovaže</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/contact">Kontakt</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/signin">Prijava
              <span class="sr-only"></span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->
  <div class="container">
    <div class="row">
      <div class="col-lg-12 text-center">
        <h1 class="mt-5">Tattoo studio</h1>
        <ul class="list-unstyled">
          <li>Tattoo</li>
        </ul>
      </div>
    </div>
    <img src="http://gotham-news.com/wp-content/uploads/2018/08/tattoo-shop-artist.jpg" width="100%" margin="0px" class="image"/>
	
	<div class="row">
            <div class="jumbotron">
            <h2>Welcome</h2>
                <p>Naše boje za tetoviranje su jake i postojane, dermatološki ispitane te su trenutno najpouzdanije boje za tetoviranje dostupne na tržištu. Stoga, osim tetovaže i piercinga, nudimo vam i lasersko uklanjanje tetovaže.

                  U našem studiju uz kvalitetan rad dobijete i vrhunski ugođaj pri samom tetoviranju uz koji možete potpuno zaboraviti na bol: jako udobna tattoo stolica, besplatan wi fi, tv, playstation 4 itd.  Konačno i ono najvažnije: sama djelatnost tetoviranja/piercinga zahtijeva visoke higijenske uvjete koje Tattoo studio strogo provodi i na kojima inzistira zbog zaštite klijenta i održavanja struke na profesionalnoj razini.</p>
            </div>
        </div>
        <!--./row-->
        <div class="row">
            <hr>
            <footer>
              <br>
                <p>&copy; 2019 {{data["developer_organization"]}}.</p>
            </footer>           
        </div>
  </div>
  
	<script>
		//example of calling custom function
		helloWorld();
	</script>
</body>
</html>