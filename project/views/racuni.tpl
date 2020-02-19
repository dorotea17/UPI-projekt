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
              <a class="dropdown-item active" href="/racuni">Računi<span class="sr-only">(current)</span></a>
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
    <div class="row" style="padding:25px 0;">
      <div class="col-md-2 text-center" style="padding: 0">
        <a href='/novi-racun' class="btn btn-secondary">Dodaj novi racun</a>
      </div>
    </div>
    <div class="row">
      <table class="table" style="background-color: white;">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Datum</th>  
            <th scope="col">Osoblje</th>
            <th scope="col">Tetovaže</th>
            <th scope="col">Ukupno</th>
            <th scope="col">Uredi</th>
            <th scope="col">Izbriši</th>
          </tr>
        </thead>
        <tbody style="background-color: white;">

            %for item in data:
            <tr>
              <th scope="row">{{item[1]._id}}</th>
              <td>{{item[1]._datum}}</td>
              <td>{{item[2]._ime}} {{item[2]._prezime}}</td>
              <td>{{item[0]._naziv}}</td>
              <td>{{item[1]._ukupno}}</td>
              <td>
                <a href='/azuriraj-racun?racuniid={{item[1]._id}}'>
                  <i class="fas fa-edit"></i>
                </a>
              </td>
              <td>
                <a href='/izbrisi-racun?racuniid={{item[1]._id}}'>
                  <i class="fas fa-trash-alt"></i>
                </a>
              </td>
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