from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///css_wizard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(days=7)

db = SQLAlchemy(app)

# Importar modelos depois de inicializar o db
from models.user import User
from models.challenge import Challenge
from models.progress import Progress

# Inicializa o banco de dados
with app.app_context():
	db.create_all()

	# Cria desafios iniciais se não existirem
	if Challenge.query.count() == 0:
		from models.seed import create_challenges

		create_challenges()

# Importar rotas (sem usar blueprints)
from routes import auth_routes, game_routes, admin_routes

if __name__ == '__main__':
	app.run(debug=True)