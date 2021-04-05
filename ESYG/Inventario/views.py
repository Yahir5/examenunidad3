from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	contenido = """
	<html>
<head>
	<title>Prueba de estilos</title>
	<style>
	div{
	color: #CD1101;
	font-size: 80px;
	text-align: center
	}
	p{
	color: #19B403;
	font-size: 60px;
	text-align: center

	}
	</style>
</head>
<body style="background-color: #0583B6", border-left: 5px solid red;>	
<div>Erick Juarez Encastin
</div>
<p>1318283314</p>
</body>
</html>

	"""

	return HttpResponse(contenido)