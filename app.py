from flask import Flask, jsonify
from flask_cors import CORS
import os

# Controllers
from core.aluno.aluno_controller import aluno_controller
from core.usuario.usuario_controller import usuario_controller
from core.professor.professor_controller import professor_controller
from core.materia.materia_controller import materia_controller

app = Flask(__name__)

# 🔧 Detecta se está rodando localmente ou no Render
is_render = os.environ.get("RENDER", None) is not None

# 🌐 Define domínios permitidos dinamicamente
if is_render:
    allowed_origins = ["https://api-escolar-react.onrender.com"]
else:
    allowed_origins = ["http://127.0.0.1:5173", "http://localhost:5173"]

# 🔓 Habilita CORS globalmente (com suporte a OPTIONS e credenciais)
CORS(
    app,
    resources={r"/*": {"origins": allowed_origins}},
    supports_credentials=True,
    allow_headers=["Content-Type", "Authorization"],
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
)

# ✅ Rota padrão (evita erro 404 em "/")
@app.route('/')
def index():
    return jsonify({"status": "API Escolar Flask online"}), 200

# 🔹 Registro dos controladores
app.register_blueprint(aluno_controller)
app.register_blueprint(usuario_controller)
app.register_blueprint(professor_controller)
app.register_blueprint(materia_controller)

if __name__ == "__main__":
    # 🚀 Use debug=False em produção
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
