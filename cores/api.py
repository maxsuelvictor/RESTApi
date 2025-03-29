from ninja import Router
from .cor_schemas import Cor
from typing import List
from produtos.models import CadTbCCor
from ninja import NinjaAPI
from django.http import HttpRequest, HttpResponse


api_local = NinjaAPI()
cores_router = Router()



@cores_router.get('/',auth=None)
def get_teste(request, response: HttpResponse):
    return {'id_item': 1}


@cores_router.post('/', auth=None)
def post_teste(request, cores: List[Cor]):
    """
    for cor in cores:
        if not cor.descricao.strip():  # Validação manual
            return api_local.create_response(request, {"error": "O campo 'descrição' não pode ser vazio."},
                                       status=400)

    novas_cores = [CadTbCCor(id_cor=cor.id_cor,descricao=cor.descricao )
                   for cor in cores]
    CadTbCCor.objects.bulk_create(novas_cores)
    #nova_cor.save()
    """
    #print(cor.id_cor)
    return {"Cor 1"}
    # Para 1 registro
      #return {"Cor adicionada:"
      #        "cor": {"id_cor": nova_cor.id_cor, "descricao": nova_cor.descricao} }
    # Para N registros
    #return {"message": "Cores adicionadas com sucesso!", "quantidade":
    #        len(novas_cores)}
