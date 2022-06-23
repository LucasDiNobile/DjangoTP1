from django.shortcuts import render
from django.http import HttpResponse 
from django.template import Template, Context, loader
from appfamilia.models import Familia


# Create your views here.

def inicio(request):
    return HttpResponse('<h1>por favor redirijase a mi-template</h1>')

def mi_template(request):
    
    template1 = loader.get_template(r'template1.html')
    
    papa = Familia(nombre='Alejandro', edad=50, lista=[1,2,3,4,5,6])
    mama = Familia(nombre='Silvana', edad=49, lista=['hola','cahu'])
    hermana = Familia(nombre='Julieta', edad=15, lista=['auto','moto','camion'])
    papa.save()
    mama.save()
    hermana.save()
    
    render1 = template1.render({'papa':papa, 'mama':mama, 'hermana':hermana})
    
    return HttpResponse(render1)