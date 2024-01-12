from flask_restful import Resource
from api import api
from..schemas import cursos_schemas
from..services import cursos_services
from flask import request, make_response, jsonify
from api.entidades.cursos_entidades import CursoEntidades

class Cursos(Resource):
    def post(self):
        novo_curso = cursos_schemas.CursoSchemas()
        validate = novo_curso.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            area = request.json['area']
            curso = CursoEntidades(nome=nome,
                                   area=area)
            cadastro_curso = cursos_services.cadastrar_cursos(curso)
            if cadastro_curso:
                return make_response(jsonify("Professor cadastrado"), 201)
            else:
                return make_response(jsonify("error: Falha no cadastro"), 500)
    def get(self):
        curso_listado = cursos_services.listar_cursos()
        carregar_validacoes = cursos_schemas.CursoSchemas(many=True)
        return make_response(carregar_validacoes.jsonify(curso_listado), 200)

class CursosDetalhes(Resource):
    def get(self, id):
        curso_desejado = cursos_services.listar_cursos_id(id)
        if curso_desejado is None:
            return make_response(jsonify("Professor não encontrado"), 404)
        else:
            carregar_validacoes = cursos_schemas.CursoSchemas()
            return make_response(carregar_validacoes.jsonify(curso_desejado), 200)

    def put(self, id):
        professor_antigo = cursos_services.listar_cursos_id(id)
        if professor_antigo is None:
            return make_response(jsonify("Professor não encontrado!"), 404)
        else:
            validacao = cursos_schemas.CursoSchemas()
            validate = validacao.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 400)
            else:
                nome = request.json['nome']
                area = request.json['area']
                novo_professor = CursoEntidades(nome=nome,
                                       area=area)
                cursos_services.atualizar_professor(professor_antigo, novo_professor)
                professor_atualizado = cursos_services.listar_cursos_id(id)
                return make_response(validacao.jsonify(professor_atualizado), 200)

    def delete(self, id):
        professor = cursos_services.listar_cursos_id(id)
        if professor is None:
            return make_response(jsonify("Professor não encontrado"), 404)
        else:
            cursos_services.deletar_professor(professor)
            return make_response(jsonify("Professor excluído com sucesso"), 204)
api.add_resource(CursosDetalhes, '/curso/<int:id>')
api.add_resource(Cursos, '/curso')