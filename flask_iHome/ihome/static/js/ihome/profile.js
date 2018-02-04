function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){});
        },1000)
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$(document).ready(function () {

    $.get("/api/v1.0/users",function (resp) {
        // 用户为登陆
        if (resp.errno == "4101"){
            location.href = "/login.html"
        } else if (resp.errno == "0"){
            $("#user-name").val(resp.data.name);
            if (resp.data.avatar) {
                $("#user-avatar").attr("src",resp.data.avatar);
            }
        }

    },"json");



    $("#form-avatar").submit(function (e) {
        // 阻止表单的默认行为
        e.preventDefault();
        // 利用jquery.form.min.js提供的ajaxSubmit对表单进行异步提交
        $(this).ajaxSubmit({
            url: "/api/v1.0/users/avatar",
            type: "post",
            dataType: "json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            success: function (resp) {
                if (resp.errno == "0") {
                    // 上传成功,将头像图片的src属性设置为图片的url
                    $("#user-avatar").attr("src", resp.data.avatar_url);
                } else if (resp.errno == "4101") {
                    // 未登录
                    location.href = "/login.html";
                } else {
                    alert(resp.errmsg)
                }
            }
        })
    });

    $("#form-name").submit(function (e) {
        // 阻止表单提交
        e.preventDefault();
        // 获取参数
        var name = $("#user-name").val();
        if (!name){
            alert('请先填写用户名');
            return;
        }

        $.ajax({
            url: "/api/v1.0/users/name",
            type: "put",
            data: JSON.stringify({name: name}),
            contentType: "application/json",
            dataType: "json",
            headers: {
                "X-CSRFTOKEN": getCookie("csrf_token")
            },
            success: function (rep) {
                if (rep.errno == "0") {
                    $(".error-msg").hide();
                    showSuccessMsg();
                } else if (rep.errno == "4003"){
                    $(".error-msg").show();
                }
            }
        })


    });



});
