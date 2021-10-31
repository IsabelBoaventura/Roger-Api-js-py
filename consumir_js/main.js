console.log("foi ");


console.log("Estamos aqui");

function fazGet( url ){
    //requisicao da url 
    let request = new XMLHttpRequest();
    request.open("GET", url, false );
    request.send();
    return request.responseText;

}


function criaLinha( usuario){
    let linha = document.createElement("tr");
    let tdId = document.createElement("td");
    let tdNome =document.createElement("td");
    tdId.innerHTML = usuario.id;
    tdNome.innerHTML = usuario.name;

    linha.appendChild(tdId);
    linha.appendChild(tdNome);

    return linha ;


}

function main(){
    let data = fazGet("http://127.0.0.1/get/usuarios");
    let usuarios =JSON.parse(data);
    let tabela = document.getElementById("tabela");
    //console.log(usuarios);
    //para cada usuario criar linha  e adicionar na tabela

    usuarios.forEach(element => {
        let linha = criaLinha(element);
        tabela.appendChild(linha);
    });

}

main();