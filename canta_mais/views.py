from django.shortcuts import render
from .models import Musica

# Create your views here.
def index(request):

    if request.POST:
        nome = request.POST['nome']
        compositor = request.POST['compositor']
        duracao = request.POST['duracao']
        quemSugeriu = request.POST["quemSugeriu"]

        musica = Musica(nome=nome, compositor=compositor, duracao=duracao, quemSugeriu=quemSugeriu)
        musica.save()

    musicas = Musica.objects.all()

    return render(request,'cadastra_musica.html', {"musicas": musicas})
