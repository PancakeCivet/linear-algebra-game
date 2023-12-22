function open_login_HTML() {
    window.close();
    window.open("login.html")
}

function open_register_HTML(){
    window.close();
    window.open("register.html")
}

function other_HTML(){
    window.close();
    localStorage.setItem("username", "游客模式");
    window.open("game.html")
}

fetch("introduction.html")
    .then(response => response.text())
    .then(data => {
        document.getElementById("about-me").innerHTML = data;
    })
    .catch(error => console.log(error));