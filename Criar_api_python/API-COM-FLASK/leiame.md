Como criar uma api em python com flask - Tutorial Python Iniciantes 1

https://www.youtube.com/watch?v=RIoC1YOY4yc

Instalar o Flask

Terminal do VSCode

### pip install flask

Importa flask no arquivo que será trabalhado ( routes.py)
<code> from flask import Flask </code>

Adiciona a aplicação
<code> app = Flask ("Youtube") </code>

Comando de Execução da aplicação
<code> app.run() </code>

Apenas com estas 3 linhas de códigos já tem o programa rodando, mesmo sem ter nada nele.

Estando na pasta onde este arquivo (routes.py) foi criado, pode abrir o terminal e adicionar o camando de execução
D:\projetos\javascrypt_e_python\Roger\Criar_api_python\API-COM-FLASK

Terminal
#### python routes.py


Criando Rotas para testes.
Rota GET 

Cria a rota
<code>@app.route("/olamundo", methods=["GET"])</code>
Cria a funcao
<code>def ola_mundo():
    return {"ola" : "mundo"}
</code>
Irá retornar com o que sera apresentado 

A cada modificação no Código rodar novamente o codigo para ele funcionar corretamente.

Para fazer o código parar de executar, digite <code> ctrl + c </code> no terminal;
Para fazer o Código voltar a rodar, digite <code> python routes.py </code> no terminal;

Verificar a rota no postman
<code>  http://127.0.0.1:5000/olamundo </code>

A rota esta certa e trouxe a mesma resposta no Postman e no Navegador. 

![image](https://user-images.githubusercontent.com/1613816/132787147-1c88e6e3-099e-4fd4-8a44-19c671bea594.png)


