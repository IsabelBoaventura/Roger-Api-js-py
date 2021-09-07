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
    situacao = db.Column(db.String(1))
    def to_json(self):
        return {
            "id_tela": self.id, 
            "nome_tela":  self.nome , 
            "email_tela": self.email,
            "situacao_tela": self.situacao
        }


# CRUD - Selecionar tudo
@app.route("/usuarios", methods=["GET"])
def seleciona_usuarios():
    usuarios_objetos = Usuario.query.all()
    # print(usuarios_objetos)
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    # para cada linha que vier de retorno do bando  será transformado em objeto json

    print(usuarios_json)
    return gera_response(200, "usuarios", usuarios_json)
    # Response( json.dumps(usuarios_json) )

# Selecionar um 
@app.route("/usuario/<id>", methods=["GET"])
def seleciona_usuario(id):
    usuario_objeto =  Usuario.query.filter_by(id=id).first()
    # para buscar o primeiro 

    usuario_json = usuario_objeto.to_json()
    return gera_response(200, "UsuarioID", usuario_json)

# Cadastrar 
@app.route("/usuario", methods=["POST"])
def cria_usuario():
    body = request.get_json()
    # validar se venho os parameros 
    # ou utilizar um try para gerar erro 
    try:
        usuario = Usuario(nome=body["nome"], email=body["email"], situacao="A")
        # para adicionar no banco de dados 
        db.session.add(usuario)
        db.session.commit()

        return gera_response(201, "Cria_usuario", usuario.to_json(), "Criado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "Cria_Usuario", {}, "Erro ao cadastrar " )



# Atualizar
@app.route("/usuario/<id>", methods = ["PUT"])
# methods PUT é o padrao para atualizacao 
def atualiza_usuario(id):
    # pegar o usuario 
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    # pegar modificacoes 
    body = request.get_json()

    # adicionar as modificacoes
    # exucutar apenas as modificacoes existentes
    try:
        if('nome' in body):
            usuario_objeto.nome = body['nome']
        if('email' in body):
            usuario_objeto.email = body['email']
        if('situacao' in body):
            usuario_objeto.situacao = body['situacao']
        
        db.session.add(usuario_objeto)
        db.session.commit()
        return gera_response(200, "Usuario_Alterado", usuario_objeto.to_json(), "Alterado com sucesso")
    except Exception as e:
        print('Erro ao alterar' , e )
        return gera_response(400, "Erro ao Alterar", {}, "Erro ao Alterar")

# Deletar
@app.route("/usuario/<id>", methods=["DELETE"])
def deleta_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()

    try:
        db.session.delete(usuario_objeto)
        db.session.commit()
        return gera_response(200, "Usuario Deletado", usuario_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro ao deletar', e)
        return gera_response(400, "Deletar Usuario", {}, "Erro ao Deletar usuario")


def gera_response(status, nome_do_conteudo, conteudo, mensagem = False ):
    body =  {}
    body[nome_do_conteudo] = conteudo
    if(mensagem):
        body["mensagem"] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")


app.run()