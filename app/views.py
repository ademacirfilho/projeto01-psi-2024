from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def index(request):
    return render(request, "index.html")

def jogadores(request):
    jogadores = [
        {"nome": "Ter Stegen", "idade": "32", "posicao": "Goleiro", "nascimento": "Monchengladbach, Alemanha", "foto": "ter-stegen.png"},
        {"nome": "Jules Koundé", "idade": "25", "posicao": "Lateral D./Zagueiro", "nascimento": "Paris, França", "foto": "jules-kounde.png"},
        {"nome": "Ronald Araújo", "idade": "25", "posicao": "Zagueiro", "nascimento": "Rivera, Uruguai", "foto": "ronald-araujo.png"},
        {"nome": "Andreas Christensen", "idade": "28", "posicao": "Zagueiro", "nascimento": "Lillerod, Dinamarca", "foto": "andreas-christensen.png"},
        {"nome": "Alejandro Balde", "idade": "20", "posicao": "Lateral Esquerdo", "nascimento": "Barcelona, Espanha", "foto": "alejandro-balde.png"},
        {"nome": "Frenkie de Jong", "idade": "27", "posicao": "Meio Campista", "nascimento": "Gorinchem, Países Baixos", "foto": "frenkie-de-jong.png"},
        {"nome": "Pedri", "idade": "21", "posicao": "Meio Campista", "nascimento": "Tegueste, Espanha", "foto": "pedri.png"},
        {"nome": "Ilkay Gundogan", "idade": "33", "posicao": "Meio Campista", "nascimento": "Gelsenkirchen, Alemanha", "foto": "ilkay-gundogan.png"},
        {"nome": "Lamine Yamal", "idade": "17", "posicao": "Ponta Direita", "nascimento": "Esplugues de Llobregat, Espanha", "foto": "lamine-yamal.png"},
        {"nome": "Robert Lewandowski", "idade": "35", "posicao": "Centroavante", "nascimento": "Varsóvia, Polónia", "foto": "robert-lewandowski.png"},
        {"nome": "Raphinha", "idade": "27", "posicao": "Ponta Direita/Esquerda", "nascimento": "Porto Alegre, Rio Grande do Sul", "foto": "raphinha.png"},
    ]

    context = {
        "jogadores": jogadores,
    }
    
    return render(request, "jogadores.html", context)

def sobre(request):
    return render(request, "sobre.html")