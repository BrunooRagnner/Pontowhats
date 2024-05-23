from flask import Flask, render_template, request
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Configuração do log de erro
formatter = logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.ERROR)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página administrativa
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Tratamento para erro 404 (página não encontrada)
@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Página não encontrada: %s', (request.path))
    return render_template('404.html'), 404

# Tratamento para erro 500 (erro interno do servidor)
@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Erro interno do servidor: %s', (error))
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)