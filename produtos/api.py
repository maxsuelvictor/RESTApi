from ninja import Router
from .schemas import Produto
from django.contrib import auth
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime, timedelta
import jwt

produtos_router = Router()

class Usuario(Produto):
    username: str
    senha: str


@produtos_router.post('/login/')
def login(request, usuario: Usuario):

    user = auth.authenticate(request, username=usuario.username,
                             password=usuario.senha)


    if not user:
        return JsonResponse({'error': 'E-mail ou senha inválidos'})


    expiration_time = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE)
    payload = {
        'user': user.username,
        'exp':  expiration_time.isoformat()
    }

    token = jwt.encode(payload, settings.SECRET_KEY_JWT, algorithm="HS256")

    return {'token': token}