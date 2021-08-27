import os
from flask import Flask, request, jsonify, send_from_directory

DIRETORIO =""

api = Flask(__name__)


@api.route("/arquivos", methods=["GET"])
def lista_arquivos():
    pass


@api.route("/arquivos/<nome_do_arquivo>", methods=["GET"])
def get_arquivo(nome_do_arquivo):
    pass


@api.route("/arquivos", methods=["POST"])
def post_arquivo():
    pass

if __name__=="__main__":
    api.run(debug=True, port=8000)