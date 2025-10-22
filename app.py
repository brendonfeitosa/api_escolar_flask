from flask import Flask
from core.aluno.aluno_controller import aluno_controller
from core.usuario.usuario_controller import usuario_controller
from core.professor.professor_controller import professor_controller
from core.materias.materias_controller import materia_controller

app = Flask(__name__)

# registro das constrollers
app.register_blueprint(aluno_controller) # estou registrando qual controlador quero registrar no meu app.py
app.register_blueprint(usuario_controller) # estou registrando qual controlador quero registrar no meu app.py
app.register_blueprint(professor_controller) # estou registrando qual controlador quero registrar no meu app.py
app.register_blueprint(materia_controller) # estou registrando qual controlador quero registrar no meu app.py

if __name__ == "__main__":
    app.run(debug=True) # mudar para debug False quando estiver em produção para que a aplicação fique um pouco mais rápida

