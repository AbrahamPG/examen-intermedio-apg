# Create your views here.
from django.shortcuts import render

def platos_list(request):
    data_context = {
            'nombre': 'Rosa Pacheco',
            'procedencia': 'Peru',
            'precio': 20.5,
        }
    return render(request, 'platos_list.html', context={'data': data_context})