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
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css">

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
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
              Tattoo Studio
            </a>
            <div class="dropdown-menu">
              <a class="dropdown-item active" href="/tattoo">Tetovaže<span class="sr-only">(current)</span></a>
              <a class="dropdown-item" href="/osoblje">Osoblje</a>
              <a class="dropdown-item" href="/racuni">Računi</a>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/odjava">Odjava</a>
              <span class="sr-only"></span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->
  <div class="container">
	<div class="row" style="margin-top: 50px;">
        <form style="width: 100%" action='{{form_akcija}}' method='POST'>

            <input type="hidden" class="form-control" id="tetovazeid" name='tetovazeid' value='{{data._id if data != None else ""}}'>

            <div class="form-group">
              <label for="link">Slika</label>
              <input type="text" class="form-control" id="link" name='link' value='{{data._link if data != None else ""}}' aria-describedby="link-help" placeholder="Unesite link" required>
            </div>

            <div class="form-group">
                <label for="naziv">Naziv</label>
                <input type="text" class="form-control" id="naziv" name='naziv' value='{{data._naziv if data != None else ""}}' aria-describedby="naziv-help" placeholder="Unesite naziv" required>
            </div>

            <div class="form-group">
              <label for="velicina">Veličina</label>
              <input type="text" class="form-control" id="velicina" name='velicina' value='{{data._velicina if data != None else ""}}' aria-describedby="velicina-help" placeholder="Unesite velicinu" required>
          </div>
            
            <div class="form-group">
                <label for="vrijeme">Vrijeme</label>
                <input type="number" class="form-control" id="vrijeme" name='vrijeme' value='{{data._vrijeme if data != None else ""}}' aria-describedby="vrijeme-help" placeholder="Unesite vrijeme" required>
            </div>

            <div class="form-group">
                <label for="cijena">Cijena</label>
                <input type="number" class="form-control" id="cijena" name='cijena' value='{{data._cijena if data != None else ""}}' aria-describedby="cijena-help" placeholder="Unesite cijenu" required>
            </div>

            <button type="submit" class="btn btn-primary" name="save">Sačuvaj</button>

        </form>     
    </div>
</body>
</html>