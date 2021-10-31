from flask import Flask, request

# modulo request usado para pegar as informações que forem adicionadas pelo methods post

app = Flask ("YouTube")

# cria a rota
@app.route("/olamundo", methods=["GET"])
# cria a funcao
def ola_mundo():
    return {"ola" : "mundo em GET"}
    # retorna com o que sera apresentado 

# methodo post , recebe informacao do Front end para o back end
# cadastro de algo 
#  # pega as informações que forem encaminhadas pelo POST
    # adiciona na nossa variavel corpo
    # traz as informações em formato json
    # # apresenta as informações no terminal

    # apresenta as informações do body para quem chaamar esta rota


@app.route("/cadastro", methods=["POST"])
def cadastraUsuario():
    body = request.get_json(force = True)
    print(body)
    return body
   

# cadastra/usuario NAO  deu certo



app.run()