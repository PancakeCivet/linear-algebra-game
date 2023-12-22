$(document).ready(function () {
    let username = localStorage.getItem("username");
    if (username === null) {
        window.location.href = "login.html";
    } 
    else {
        let temp_username = "欢迎您，";
        $(".username").text(temp_username + username); // concatenate temp_username and username
    }

    $(".logout-button").click(function () {
        localStorage.clear();
    });
    
    $("#out").click(function () {
        window.close();
        window.open("homepage.html");
    });
});
