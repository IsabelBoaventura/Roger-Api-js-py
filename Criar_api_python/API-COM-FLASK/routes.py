from flask import Flask

app = Flask ("YouTube")

# cria a rota
@app.route("/olamundo", methods=["GET"])
# cria a funcao
def ola_mundo():
    return {"ola" : "mundo"}
    # retorna com o que sera apresentado 

# methodo post , recebe informacao do Front end para o back end

def cadastra_usuario():
    return {"id": 0}
app.run()