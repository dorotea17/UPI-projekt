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
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet">

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
            <a class="nav-link" href="/recenzije">Recenzije
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/odjava">Odjava</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->

  <div class="container">
  <div class="row" style="margin-top: 50px;">
    <div class="col-lg-12 text-center">
      <h1 class="mt-5">Recenzija</h1>
    </div>
      <form style="width: 100%" action='{{form_akcija}}' method='POST'>
        <div class="rating">
            <input type="radio" name="star" id="star1"><label for="star1"></label>
            <input type="radio" name="star" id="star2"><label for="star2"></label>
            <input type="radio" name="star" id="star3"><label for="star3"></label>
            <input type="radio" name="star" id="star4"><label for="star4"></label>
            <input type="radio" name="star" id="star5"><label for="star5"></label>
          </div>
          <br><br><br><br><br><br>
            <button type="submit" class="btn btn-primary" name="save">Sačuvaj</button>

        </form>     
	</div>
    </div>
</body>
</html>