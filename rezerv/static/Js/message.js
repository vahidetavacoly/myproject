
function setdata(caption, id)
{
    $("#id_caption").val(caption);
   
    $("#id_id").val(id);
}

console.log("hello");

function creature(caption)
{
    $("#id_caption").val("");

    $("#id_id").val("0");
}

$(document).ready(function() {
    $(".savedata").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/create_message",
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
            url: "http://" + window.location.host + "/delet_message",
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
function getdata1(ferstande_id) {
    $("#ferstande_id").val(ferstande_id); // Corrected the value to use the parameter soal_id
    }
function getdata2(girande_id) {
        $("#girande_id").val(girande_id); // Corrected the value to use the parameter soal_id
        }
    


