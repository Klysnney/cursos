from api import MA
from..models import cursos_models
from marshmallow import fields

class CursoSchemas(MA.SQLAlchemySchema):
    class Meta:
        model = cursos_models.CursoModel
        load_instance = True
        fields = ('id', 'nome', 'area')

    nome = fields.String(required=True)
    area = fields.String(required=True)