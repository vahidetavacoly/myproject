
//پادکست
function setdata(name,soal,result ,id)
{
    $("#id_name").val(name);
    $("#id_soal").val(soal);
    $("#id_result").val(result);
    $("#id_id").val(id);
}

console.log("hello");

function creature(name,soal,result)
{
    $("#id_name").val("");
    $("#id_soal").val("");
    $("#id_result").val();
    $("#id_id").val("0");
}
//پادکست
$(document).ready(function() {
    $(".savedata").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/create_test",
            data: $(".frm").serialize(),
            beforeSend: function() { // Corrected beforesend to beforeSend
                $(".result").html("در حال ارسال .....");
            },
            success: function(result) {
                if (result == "true") {
                    $(".result").html("ثبت اطلاعات انجام شد ");
                } else {
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
            url: "http://" + window.location.host + "/delet_test",
            data: $(".frm-delet").serialize(),
            success: function(result) {
                if (result == "true") {
                    $(".result-delet").html("حذف اطلاعات انجام شد ");
                } else {
                    $(".result-delet").html("خطا");
                }
            },
            error: function(e) {
                $(".result-delet").html("مشکلی در حذف رخ داد ");
            }
        });
    });

});

