from api import db

class CursoModel(db.Model):
    __tablename__ = "cursos"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True, nullable = False)
    nome = db.Column(db.String(50), nullable=False)
    area = db.Column(db.String(50), nullable=False)