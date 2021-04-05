from django.shortcuts import render
from examen.models import nombre
# Create your views here.
def inicio(request):
	producto = nombre.objects.all()
	return render(request,"home.html",{"producto":producto})

