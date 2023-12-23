# Create your views here.
from django.shortcuts import render

def meseros_list(request):
    data_context = {
            'nombre': 'Emilio Pacheco',
            'edad': 20,
            'dni': "3214567",
            'pais': "Perú",
        }

    return render(request, 'meseros_list.html', context={'data': data_context})