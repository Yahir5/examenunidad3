from django.shortcuts import render,HttpResponse
from tienda.models import Productos
# Create your views here.
def inicio(request):
	producto = Productos.objects.all()
	return render(request,"index.html",{"producto":producto})