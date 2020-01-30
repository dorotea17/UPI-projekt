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
              <li class="nav-item" id="about">
                <a class="nav-link" href="/about">O nama</a>
              </li>
              <li class="nav-item active">
                <a class="nav-link" href="/tetovaze">Tetovaže<span class="sr-only">(current)</span></a>
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
    <div class="row" style="padding:25px 0;">
      <div class="col-md-2 text-center" style="padding: 0">
      </div>
  </div>
    <div class="row">
      <table class="table" style="background-color: white;">
        <thead>
          <tr>
            <th scope="col">Slika</th>  
            <th scope="col">Naziv</th>
            <th scope="col"><a href="/tetovaze">Veličina</a><br>
                <li><a href="/velika">Velika</a></li>
                <li><a href="/mala">Mala</a></li>
            </th>
            <th scope="col">Vrijeme</th>
            <th scope="col">Cijena
            </th>
          </tr>
        </thead>
        <tbody style="background-color: white;">

            %for item in data:
            <tr>
              <td><img src="{{item._link}}" height="200px" width="200px"></td>
              <td>{{item._naziv}}</td>
              <td>{{item._velicina}}</td>
              <td>{{item._vrijeme}}</td>
              <td>{{item._cijena}}</td>
            </tr>

            %end
        </tbody>
      </table>
    </div>
  </div>
  
	<script>
		//example of calling custom function
		helloWorld();
	</script>
</body>
</html>