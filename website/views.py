from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html')

def elenco(request):

    li_elenco = [
        {"Personagem":"Yuichi","Ator":"Hayato Ichihara","papel":"Protagonista","nasc":"Nascido em 1987, Tóquio, Japão"},
        {"Personagem":"Shugo Oshinari","Ator":"Shugo Oshinari","papel":"Antagonista","nasc":"Nascido em 1983, Kanagawa, Japão"},
        {"Personagem":"Shiori Tsuda","Ator":"Ayumi Ito","papel":"Personagem feminina central","nasc":"Nascida em 1985, Osaka, Japão"},
        {"Personagem":"Lily Chou-Chou (voz)","Ator":"Salyu","papel":"A cantora fictícia do filme","nasc":"Nascida em 1983, Hokkaidō, Japão"},
        {"Personagem":"Chie Moritaka","Ator":"Miwako Ichikawa","papel":"Colega de escola","nasc":"Nascida em 1989, Saitama, Japão"},
        {"Personagem":"Izumi Inamori","Ator":"Kuno Yukawa","papel":"Colega vítima de bullying","nasc":"Nascida em 1977, Aichi, Japão"},
    ]

    context = {
        "atores": li_elenco,
    }

    return render(request, 'website/elenco.html', context)

def sobre(request):
    return render(request, 'website/sobre.html')
