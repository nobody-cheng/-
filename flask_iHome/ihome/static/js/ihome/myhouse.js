$(document).ready(function () {
    $.get("/api/v1.0/users/auth", function (resp) {
        if (resp.errno == "4101") {
            location.href = "/login.html";
        } else if (resp.errno == "0") {
            // 已登陆未认证
            if (!(resp.data.real_name && resp.data.id_card)) {
                $(".auth-warn").show();
                return;

            }

            $.get("/api/v1.0/users/auth",function (resp) {
                if (resp.errno =="0"){
                    // 未写完,发布房源实名认证
                    $("#auth-warn").hide()
                }
            })
        }
    });



});