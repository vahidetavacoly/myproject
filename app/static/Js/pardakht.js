//پادکست
function setdata(mablagh, id)
{
    $("#id_mablagh").val(mablagh);

    $("#id_id").val(id);
}

console.log("hello");

function creature(mablagh)
{
    $("#id_mablagh").val("");
   
    $("#id_id").val("0");
}
//پادکست
$(document).ready(function() {
    $(".savedata").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/create_pardakht",
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

    
});

