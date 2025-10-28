from flask import Flask
from flask_cors import CORS
import os
from core.aluno.aluno_controller import aluno_controller
from core.usuario.usuario_controller import usuario_controller
from core.professor.professor_controller import professor_controller
from core.materia.materia_controller import materia_controller

app = Flask(__name__)

# 🔧 Detecta se está rodando localmente ou no Render
# O Render define a variável de ambiente 'RENDER' automaticamente
is_render = os.environ.get("RENDER", None) is not None

# Define o domínio permitido dinamicamente
if is_render:
    allowed_origins = ["https://api-escolar-react.onrender.com"]
else:
    allowed_origins = ["http://127.0.0.1:5173", "http://localhost:5173"]

# 🔓 Habilita CORS (acesso cruzado) com base no ambiente
CORS(app, origins=allowed_origins)

# registro das constrollers
app.register_blueprint(aluno_controller) # estou registrando qual controlador quero registrar no meu app.py
app.register_blueprint(usuario_controller) # estou registrando qual controlador quero registrar no meu app.py
app.register_blueprint(professor_controller) # estou registrando qual controlador quero registrar no meu app.py
app.register_blueprint(materia_controller) # estou registrando qual controlador quero registrar no meu app.py

if __name__ == "__main__":
    app.run(debug=True) # mudar para debug False quando estiver em produção para que a aplicação fique um pouco mais rápida

