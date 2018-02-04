function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function () {
        setTimeout(function () {
            $('.popup_con').fadeOut('fast', function () {
            });
        }, 1000)
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function () {

    $.get("api/v1.0/useres", function (resp) {
        // 4101代表用户未登录

        if (resp.errno == "4101") {
            location.href = "/login.html";
        }
        else if (resp.errno == "0") {
            // 如果返回的数据中real_name与id_card不为null，表示用户有填写实名信息
            if (resp.data.real_name && resp.data.id_card) {
                $("#real-name").val(resp.data.real_name);
                $("#id-card").val(resp.data.id_card);
                // 给input添加disabled属性，禁止用户修改
                $("#real-name").prop("disabled", true);
                $("#id-card").prop("disabled", true);
                // 隐藏提交保存按钮
                $("#form-auth>input[type=submit]").hide();
            }
        }
    }, "json");


    // 提交实名认证表单
    $("#form-auth").submit(function (e) {
        e.preventDefault();
        if ($("#real-name").val() == "" || $("#id-card").val() == "") {
            $(".error-msg").show();
        }

        // 将表单的数据转换为json字符串
        var data = {};
        $(this).serializeArray().map(function (x) {
            data[x.name] = x.value;
        });
        var jsonData = JSON.stringify(data);

        $.ajax({
            url: "/api/v1.0/users/auth",
            type: "post",
            data: jsonData,
            dataType: "json",
            contentType: "application/json",
            headers: {
                "X-CSRFTOKEN": getCookie("csrf_token")
            },
            success: function (resp) {
                if (resp.errno == 0) {
                    $(".error-msg").hide();
                    // 显示保存成功
                    showSuccessMsg();
                    $("#real-name").prop("disable", true);
                    $("#id-card").prop("disable", true);
                    $("#form-auth>input[type=submit]").hide();

                }
            }
        })


    });


});