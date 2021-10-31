function fasPost(url, body ){
    console.log("Body= ", body);
    //passar para o servidor
    let request = new XMLHttpRequest();
    request.open("POST", url,  true) ;
    request.setRequestHeader("Content-type", "application/json");
    request.send(JSON.stringify(body));
    
    request.onload = function(){
        console.log(this.responseText);
    }

    return request.responseText;
    
}

function cadastraUsuario(){
    event.preventDefault();
    let url="http://127.0.0.1:5000/users";
    let nome = document.getElementById("nome").value;
    let email = document.getElementById("email").value;
    console.log( nome , email) ;
    body = {
        "name" : nome,
        "email": email
    }
    fasPost( url , body);
}