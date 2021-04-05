from django.shortcuts import render
from django.http import HttpResponse
import random
import datetime
# Create your views here.

def principal(request):
	contenido = """ <html>
	<head>
	<body>
	<h1>Bienvenido</h1>
	<a href='numeros'>Numeros aleatorios</a>
	<a href='hora'>Hora del servidor/a>
	</body>
	</head>
	</html>"""
	return HttpResponse(contenido)

	def aleatorio(request):
		num1 = random.randit(1,11)
		num2 = random.randit(1,11)
		suma = num1 + num2
		resultado = "La suma es de: "+str(num1) + "+" +str(num2)+
		contenido = """<html>
		<head>
		</head>
		<body>
			<h1>%s</h1>
		</body>
		</html>"""%resultado
		return HttpResponse(contenido)

		def hora(request):
		actual = datetime.datetime.now()
		contenido = """<html>
		<head>
		</head>
		<body>
			<h1>La hora y fecha son: %s</h1>
		</body>
		</html>"""%resultado
		return HttpResponse(contenido)