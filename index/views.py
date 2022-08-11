
from django.shortcuts import render , redirect


# Create your views here.
def piedra_papel_tijera_view(request):

    return render(request, 'piedra-papel-tijera.html')



