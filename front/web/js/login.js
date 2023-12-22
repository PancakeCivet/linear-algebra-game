$(document).ready(function () {
      // 点击注册链接
    $("#goToRegister").click(function () {
        window.location.href = "http://127.0.0.1:5500/front/web/register.html"; // 修改为注册页面的URL
    });

    // 点击登录按钮
    $("#submit").click(function () {
        event.preventDefault();
        let password = $("#password").val();
        let username = $("#username").val();
        let data = { "username": username, "password": password };
        let data_json = JSON.stringify(data);
        $("#password").next("p").remove();
        $("#username").next("p").remove();

        $.ajax({
            url: "http://127.0.0.1:8082/login",
            type: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data: data_json,
            success: function (type) {
                if (type == 1) {
                    localStorage.setItem("username", username);
                    window.open("game.html");
                    // 添加历史记录
                    pushHistory();
                }
                if (type == 2)
                    $("#password").after("<p style='color: red;'>密码错误</p>");
                if (type == 3)
                    $("#username").after("<p style='color: red;'>用户名错误</p>");
            }
        });
    });

});
