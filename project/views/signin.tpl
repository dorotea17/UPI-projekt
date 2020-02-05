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
          <li class="nav-item">
            <a class="nav-link" href="/">Početna
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/about">O nama
              <span class="sr-only"></span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/tetovaze">Tetovaže</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/contact">Kontakt</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
              Prijava
            </a>
            <div class="dropdown-menu">
              <a class="dropdown-item active" href="/signin">Sign in<span class="sr-only">(current)</span></a>
              <a class="dropdown-item" href="/signup">Sign up</a>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->
  <div class="container">
    <div class="row">
      <div class="col-lg-12 text-center">
        <h1 class="mt-5">Prijava</h1>
    </div>
    <div class="container">
        <div class="row" style="margin-top: 50px; padding-top: 30px; font-size: 20px;">
        <form style="width: 100%" action='{{form_akcija}}' method="POST">    
        <label for="e_mail">Email</label>
        <input type="email" class="form-control" id="e_mail" name='e_mail' placeholder="Unesite email..." required width="80%">
        <br>
        <label for="lozinka">Lozinka</label>
        <input type="password" class="form-control" id="lozinka" name='lozinka' placeholder="Unesite lozinku..." required width="80%">
        <button class="btn btn-secondary" type="submit" style="width:120px;height:40px;margin-top: 20px;">Login</button><br><br>
      </form>
        </div>
    </div>

  </div>
</div>
	<script>
		//example of calling custom function
		helloWorld();
	</script>
</body>
</html>