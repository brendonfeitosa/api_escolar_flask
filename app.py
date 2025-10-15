from flask import Flask
from core.aluno.aluno_controller import aluno_controller

app = Flask(__name__)

# registro das constrollers
app.register_blueprint(aluno_controller) # estou registrando qual controlador quero registrar no meu app.py

if __name__ == "__main__":
    app.run(debug=True) # mudar para debug False quando estiver em produção para que a aplicação fique um pouco mais rápida

