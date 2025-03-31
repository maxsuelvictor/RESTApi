from ninja import Router
from .schemas import Produto
from django.http import HttpRequest, HttpResponse
from time import sleep

produtos_router = Router()

# @produtos_router.post('/')
# Especificando o auth=None, a chamada desse endpoint não irá passar pela
# autenticação, a escolha é sua
@produtos_router.get('/', auth=None)
def get_teste(request, response: HttpResponse):
    return {'id_item':1 }
    #print(produto.id_item)

    # Se for usar a autenticação o código deve ter o request abaixo
    #return {'id_item': 1, 'request': request.auth}


 #Exemplo de post
@produtos_router.post('/')
def post_teste(request):
    #print(produto.id_item)
    return  {'id_item': 1}
