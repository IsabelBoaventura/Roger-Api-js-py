from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/banco_usuario'

db = SQLAlchemy(app)

# Criar a tabela no banco de Dados
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))

# CRUD - Selecionar tudo

# Selecionar um 
# Cadastrar 
# Atualizar
# Deletar


app.run()