from..models import cursos_models
from api import db

def cadastrar_cursos(novo_curso):
    curso_cadastrar = cursos_models.CursoModel(nome=novo_curso.nome,
                                               area=novo_curso.area)
    db.session.add(curso_cadastrar)
    db.session.commit()
    return curso_cadastrar

def listar_cursos():
    cursos = cursos_models.CursoModel.query.all()
    return cursos

def listar_cursos_id(id):
    curso_especificado = cursos_models.CursoModel.query.filter_by(id=id).first()
    return curso_especificado

def atualizar_professor(professor_antigo, professor_novo):
    professor_antigo.nome = professor_novo.nome
    professor_antigo.area = professor_novo.area
    db.session.commit()

def deletar_professor(id):
    db.session.delete(id)
    db.session.commit()