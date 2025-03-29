from ninja import Schema
from django.core.exceptions import ValidationError


class Cor(Schema):
    id_cor: int
    descricao: str

    """def validate(self):
        if not self.descricao.strip():
            raise ValidationError("O campo 'descrição' não pode ser vazio.")
    """