
function setdata(title, caption,audio, id)
{
    $("#id_title").val(title);
    $("#id_caption").val(caption);
    $("#id_audio").val(audio);
    $("#id_id").val(id);
}

console.log("gthyhjyjyghythyh");

function creature(title, caption,audio)
{
    $("#id_title").val("");
    $("#id_caption").val("");
    $("#id_audio").val("");
    $("#id_id").val("0");
}
console.log("jjjjjjjjjjjjjjj");
$(document).ready(function() {
    $(".savedata").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/create_padcast",
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
            url: "http://" + window.location.host + "/delet_padcast",
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

