from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

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
    p = get_object_or_404(Produto, id = pk)
    context = {
        'p' : p
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type= 'text/html; charset=utf8', status = 404)

def error500(request, ex):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type= 'text/html; charset=utf8', status = 500)