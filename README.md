# Roger-Api-js-py

Python Flask API upload e download Arquvios - Salvar e Baixar arquivo com Python

Baseado em: https://github.com/vieiraroger/flask-salvar-arquivos

https://www.youtube.com/watch?v=oKtJdsFfNnI

# Baixando o arquivo
![image](https://user-images.githubusercontent.com/1613816/131062213-13b9a8da-bd06-4e9a-9dbd-631c609ef962.png)


# Segundo Parte
## CRUD
CRUD COMPLETO FLASK com SQLALCHEMY em Python - API REST e BANCO DE DADOS 2021

https://www.youtube.com/watch?v=WDpPGFkI9UU

Instalar bibliotecas:


>>> flask
    Instalar
        pip install flask
>>> flask_sqlalchemy
        pip install flask_sqlalchemy
>>> mysql-connector-python
        pip install mysql-connector-python
>>> mysqlclient
        pip install mysqlclient

Para atualizar a minha versão do python
    c:\python39\python.exe -m pip install --upgrade pip


Dentro do app.py
>>> from flask import Flask, Reponse, request 
onde o FLASK  será para criar as rotas do API 
RESPONSE para o retorno do Api
request para trabalhar com as respostas 

>>> from flask_sqlalchemy import SQLAlchemy
classe que ira trabalhar com o banco de dados 


Banco de Dados: usuario
Tabela: usuarios

CREATE TABLE `usuario`.`usuarios` (
    `Id` INT NULL AUTO_INCREMENT PRIMARY KEY, 
    `Nome` VARCHAR(30) NOT NULL, 
    `Email` VARCHAR(50) NOT NULL
) ENGINE = MyISAM;


Para gerar a tabela pelo codigo pode usar  db.created_all()
Entretanto, se este codigo estiver dentro do sistema, toda a vez que o sistema for reiniciado,
ele pode tentar criar a tabela novametne,  
NÃO recomendável que seja feito assim 

Recomendado criar pelo Terminal pip

>>> python 
mostra as informações do python e permite que executamos codigos do python 

>>> from app import db
>>> db.create_all()

para sair do módulo de edição do python 
>>> exit()




# CRUD 

criei o banco Manualmente 
CREATE DATABASE `banco_usuario` ;

@app.route("/usuarios", method=["GET"])
def seleciona_usuarios():
    usuarios_classe = Usuario.query.all()
    print( usuarios_classe)
    

return Response()



para rodar 
>>> python .\app.py


testar no postman

http://127.0.0.1:5000/usuarios


Depois de corrigido todos os erros,  entre eles Columm no lugar de Column para a situacao
e criada a coluna situacao direto no banco de dados,  agora o postman esta respondendo com a resposta 200 
 uhuu 

Conseguimos fazer a requisição ao postman
agora temos de trazer as informações 











Acesso com o postman

![image](https://user-images.githubusercontent.com/1613816/132132426-23ce15eb-28d8-4c7b-89fa-7ea58223f4cc.png)


