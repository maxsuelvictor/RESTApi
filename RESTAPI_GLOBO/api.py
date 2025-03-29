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

"""
class MyAuth(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str):
        return True
# --- é tipo de autenticação Global, serve para todos os endpoint
# --- todas as API irá passar por ela
api = NinjaAPI(auth=MyAuth())
"""

# Aula 17 - Basic auth 01
class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        print(username, password)
        return 1



api = NinjaAPI(auth=BasicAuth())

api.add_router('/produtos',produtos_router)
api.add_router('/cores',cores_router)