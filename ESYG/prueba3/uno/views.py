from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
# Create your views here.

def suma(request,num1,num2):
	res = num1+num2
	contenido = """
	<html>
		<head> 
		<body>
			<h2>El resultado es: %s </h2>

		</body></head>
	</html>
	 """ %res
	return HttpResponse(contenido)

def prueba1(request):
	externo = open("C:/Users/erick/OneDrive/Escritorio/Trabajos Django/ESYG/templates/prueba.html")
	plantilla = Template(externo.read())
	externo.close()
	ctx = Context()
	contenido = plantilla.render(ctx)
	return HttpResponse(contenido)
	
def prueba2(request):
	return render(request,"prueba.html")

