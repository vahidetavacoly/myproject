
function setdata(title,caption, id)
{
 
    $("#id_title").val(title);
    $("#id_caption").val(caption);
    $("#id_id").val(id);
}

console.log("hello");

function creature(title,caption)
{
    $("#id_title").val("");
    $("#id_caption").val("");
    $("#id_id").val("0");
}

$(document).ready(function() {
    $(".savedata").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/create_Faq",
            data: $(".frm").serialize(),
            beforeSend: function() { // Corrected beforesend to beforeSend
                $(".result").html("در حال ارسال .....");
            },
            success: function(result) {
                if (result == "true") {
                    $(".result").html("ثبت اطلاعات انجام شد ");
                }else {
                    $(".result").html("مشکلی در ثبت رخ داد ");
                }
            },
            error: function(e) {
                $(".result").html("مشکلی  رخ داد ");
            }
        });
    });

    $(".ok_delet").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/delete_Faq",
            data: $(".frm-delet").serialize(),
            success: function(result) {
                if (result == "true") {
                    $(".result-delet").html("حذف اطلاعات انجام شد ");
                }else{
                    $(".result-delet").html("خطا");
                }
            },
            error: function(e) {
                $(".result-delet").html("مشکلی در حذف رخ داد ");
            }
        });
    });
    $(".savej").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/create_answer",
            data: $(".formj").serialize(),
            beforeSend: function() {
                $(".resultj").html("در حال ارسال .....");
            },
            success: function(result) {
            console.log(result);
                if (result == "true") {
                    $(".resultj").html("ثبت اطلاعات انجام شد ");
                } else {
                    $(".resultj").html("مشکلی  رخ داد ");
                }
            },
            error: function(e) {
                $(".resultj").html("مشکلی در ثبت رخ داد ");
            },
        });
    });

});
function getdata(soal_id) {
    $("#soal_id").val(soal_id); // Corrected the value to use the parameter soal_id
    }
