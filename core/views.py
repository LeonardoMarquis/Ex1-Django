from django.shortcuts import render

from core.models import Produto

# Create your views here.

def index(request):
    produtos_list = Produto.objects.all()

    print(dir(request))
    print(f'Headers: {request.headers}\n')
    print(f'User-Agent: {request.headers['User-Agent']}\n')
    print(f'User: {request.user}')
    print(dir(request.user))
    if str(request.user) != "AnonymousUser":
        print(request.user.email)
        print(request.method)
        teste = 'Usuario logado'
    else:
        teste = 'Usuário não logado'
    context = {
        'logado' : teste,
        'produtos_list' : produtos_list
    }

    return render(request, 'index.html', context)

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def user_terms(request):
    return render(request, 'user_terms.html')


def produto(request, pk):
    p = Produto.objects.get(id = pk)
    context = {
        'p' : p
    }
    return render(request, 'produto.html', context)
