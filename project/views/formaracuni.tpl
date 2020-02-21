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
              <a class="dropdown-item" href="/tattoo">Tetovaže</a>
              <a class="dropdown-item" href="/osoblje">Osoblje</a>
              <a class="dropdown-item active" href="/racuni">Računi<span class="sr-only">(current)</a>
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

            <input type="hidden" class="form-control" id="racuniid" name='racuniid' value='{{data[1]._id if data != None else ""}}'>

            <div class="form-group">
                <label for="datum">Datum</label>
                <input type="date" class="form-control" id="datum" name='datum' value='{{data[1]._datum if data != None else ""}}' aria-describedby="datum-help" placeholder="Unesite datum" required>
            </div>

            <label for="osoblje">Osoblje</label><br>
            <select class="selectpicker form-control" type="text" id="osoblje" name="osoblje" style="height: 40px;"></select>
            <script>
              var select = document.getElementById("osoblje");
              var options = {{!podaciO}} 
            
              for(var i = 0; i < options.length; i++) {
                var opt = options[i];
                var el = document.createElement("option");
                el.textContent = opt;
                el.value = opt;
                select.appendChild(el);
              }
            </script><br>
            
            <label for="tetovaze">Tetovaža</label><br>
            <select class="selectpicker form-control" type="text" id="tetovaze" name="tetovaze" style="height: 40px;"></select>
            <script>
              var select = document.getElementById("tetovaze");
              var options = {{!podaciT}}
              
              for(var i = 0; i < options.length; i++) {
                var opt = options[i];
                var el = document.createElement("option");
                el.textContent = opt;
                el.value = opt;
                select.appendChild(el);
              }
            </script><br>
            <div class="form-group">
                <label for="ukupno">Ukupno</label>
                <input type="number" class="form-control" id="ukupno" name='ukupno' value='{{data[1]._ukupno if data != None else ""}}' aria-describedby="ukupno-help" placeholder="Unesite ukupan iznos" required>
            </div>

            <button type="submit" class="btn btn-primary" name="save">Sačuvaj</button>

        </form>     
    </div>

</body>
</html>