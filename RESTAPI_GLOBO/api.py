# REST API COM DJANGO NINJA
# Esse projeto faz parte do curso
from typing import Optional, Any

from django.http import HttpRequest
from ninja import NinjaAPI
from produtos.api import produtos_router
from cores.api import cores_router
#--- Faz parte da aula da AULA 15 - RECEBENDO O TOKEN...
from ninja.security import HttpBearer
#-------------------------------------------------------

# Aula 17 - Basic auth 01
from ninja.security import HttpBasicAuth
#

# Aula 18 - Basic auth 01
from django.contrib import auth
#



"""
class MyAuth(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str):
        return True
# --- é tipo de autenticação Global, serve para todos os endpoint
# --- todas as API irá passar por ela
api = NinjaAPI(auth=MyAuth())
"""

# Aula 17 - Basic auth 01
"""
class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        # Aqui vc pode buscar as informações no seu cadastro de usuário
          #pra verificar o usuário e a senha
        # esse user faz parte da tabela de User do Django admin
        #user = auth.authenticate(username=username, password=password)
        print(username, password)
        print(str(user.id))
        return 1
"""


#api = NinjaAPI(auth=BasicAuth())
api = NinjaAPI()


api.add_router('/produtos',produtos_router)
api.add_router('/cores',cores_router)