
function setk(name,family,cod_meli,mahal_tavalod,datetime,namepedar,tahsilatpedar,shoghlepedar,telpedar,adress_p,namemadar,tahsilatmadar,shoghlmadar,telmadar,telsabet,adress_m,adressmanzel,codeposti,vatsap,imagk,id)
{
         $("#id_name").val(name);
         $("#id_family").val(family);
         $("#id_cod_meli").val(cod_meli);
         $("#id_mahal_tavalod").val(mahal_tavalod);
         $("#id_datetime").val(datetime);
         $("#id_namepedar").val(namepedar);
         $("#id_tahsilatpedar").val(tahsilatpedar);
         $("#id_shoghlepedar").val(shoghlepedar);
         $("#id_telpedar").val(telpedar);
         $("#id_adress_p").val(adress_p);
         $("#id_namemadar").val(namemadar);
         $("#id_tahsilatmadar").val(tahsilatmadar);
         $("#id_shoghlmadar").val(shoghlmadar);
         $("#id_telmadar").val(telmadar);
         $("#id_telsabet").val(telsabet);
         $("#id_adress_m").val(adress_m);
         $("#id_adressmanzel").val(adressmanzel);
         $("#id_codeposti").val(codeposti);
         $("#id_vatsap").val(vatsap);
         $("#id_imagk").val(imagk);
         $("#id_id").val(id);



}
function creatk(name,family,cod_meli,mahal_tavalod,datetime,namepedar,tahsilatpedar,shoghlepedar,telpedar,adress_p,namemadar,tahsilatmadar,shoghlmadar,telmadar,telsabet,adress_m,adressmanzel,codeposti,vatsap,imagk)
{        $("#id_name").val("");
         $("#id_family").val("");
         $("#id_cod_meli").val("");
         $("#id_mahal_tavalod").val("");
         $("#id_datetime").val("");
         $("#id_namepedar").val("");
         $("#id_tahsilatpedar").val("");
         $("#id_shoghlepedar").val("");
         $("#id_telpedar").val("");
         $("#id_adress_p").val("");
         $("#id_namemadar").val("");
         $("#id_tahsilatmadar").val("");
         $("#id_shoghlmadar").val("");
         $("#id_telmadar").val("");
         $("#id_telsabet").val("");
         $("#id_adress_m").val("");
         $("#id_adressmanzel").val("");
         $("#id_codeposti").val("");
         $("#id_vatsap").val("");
         $("#id_imagk").val("");
         $("#id_id").val("0");
}

         

function setp(name,family,cod_meli,mahal_tavalod,datetime,mizantahsilat,reshtetasili,doreamozeshi,sabeghekar,savabeghshoghli,semat,elattarkkar,semataknon,tahol,namehamsar,tedadfarzand,tel,telsabet,adress_m,imagp,id)
{
         $("#id_name").val(name);
         $("#id_family").val(family);
         $("#id_cod_meli").val(cod_meli);
         $("#id_mahal_tavalod").val(mahal_tavalod);
         $("#id_datetime").val(datetime);
         $("#id_mizantahsilat").val(mizantahsilat);
         $("#id_reshtetasili").val(reshtetasili);
         $("#id_shoghlepedar").val(shoghlepedar);
         $("#id_doreamozeshi").val(doreamozeshi);
         $("#id_sabeghekar").val(sabeghekar);
         $("#id_savabeghshoghli").val(savabeghshoghli);
         $("#id_semat").val(semat);
         $("#id_elattarkkar").val(elattarkkar);
         $("#id_semataknon").val(semataknon);
         $("#id_tahol").val(tahol);
         $("#id_namehamsar").val(namehamsar);
         $("#id_tedadfarzand").val(tedadfarzand);
         $("#id_tel").val(tel);
         $("#id_telsabet").val(telsabet);
         $("#id_adress_m").val(adress_m);
         $("#id_imagp").val(imagp);
         $("#id_id").val(id);
}


function creatp(name,family,cod_meli,mahal_tavalod,datetime,mizantahsilat,reshtetasili,doreamozeshi,sabeghekar,savabeghshoghli,semat,elattarkkar,semataknon,tahol,namehamsar,tedadfarzand,tel,telsabet,adress_m,imagp)
{
         $("#id_name").val("");
         $("#id_family").val("");
         $("#id_cod_meli").val("");
         $("#id_mahal_tavalod").val("");
         $("#id_datetime").val("");
         $("#id_mizantahsilat").val("");
         $("#id_reshtetasili").val("");
         $("#id_shoghlepedar").val("");
         $("#id_doreamozeshi").val("");
         $("#id_sabeghekar").val("");
         $("#id_savabeghshoghli").val("");
         $("#id_semat").val("");
         $("#id_elattarkkar").val("");
         $("#id_semataknon").val("");
         $("#id_tahol").val("");
         $("#id_namehamsar").val("");
         $("#id_tedadfarzand").val("");
         $("#id_tel").val("");
         $("#id_telsabet").val("");
         $("#id_adress_m").val("");
         $("#id_imagp").val("");
         $("#id_id").val("0");
}


$(document).ready(function() {
    $(".savedata").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/create_Faq",
            data: $(".frmf").serialize(),
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
                $(".result").html("مشکلی در ثبت رخ داد ");
            }
        });
    });

    $(".ok_delet").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/delet_Faq",
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
                    $(".resultj").html("مشکلی در ثبت رخ داد ");
                }
            },
            error: function(e) {
                $(".resultj").html("مشکلی در ثبت رخ داد ");
            },
        });
    });
   
    $(".savedatap").click(function(){

      $.ajax({

                  type:"POST",
                  url:"http://" + window.location.host + "/create_moshaver",
                  data: $(".frm").serialize(),
                  beforesend:function() {
                      $(".result").html("در حال ارسال .....");   },

                  success: function(result){
                      if (result=="true"){
                          $(".result").html("ثبت اطلاعات انجام شد ");
                      }


                      else{
                          $(".result").html("مشکلی در ثبت رخ داد  ");
                      }
                     },
                  error:function (e) {
                          $(".result").html("مشکلی در ثبت رخ داد  ");  }

          });

         });
    $(".ok_deletp").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/delet_moshaver",
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


$(document).addEventlistener('DOMContetLoaded',function(){
        const filterButton=document.getElementSelectorAll('#filter-buttons button');
        const images=document.querySelectorAll('image-gallery img');
        filterButtons.forEach(button=>{
            button.addEventlistener('click',function(){
                const category=this.dataset.category;
                images.forEach(image=>{
                    //اگر کتگوری allانتخاب شود همه را نمایش دهد
                    if(category==='all'){
                        images.classList.remove('hidden')
                    }else{
                        //در غیر این صورت فقط تصاویر مربوط به ان دسته بندی نمایش داه میشود
                        if(image.classList.contains(category)){
                            image.classList.remove('hidden');
                        }else{
                            
                    
                        image.classList.add('hidden');
                    }
                }
                });
            });
          
        });
});   
function showModel(modelid){
    const models=document.querySelectorAll('.images');
    modelid.forEach(model=>model.classList.add('hidden'));
    const selectedModel=document.getElementById(modelid);
    if (selectedModel){
        selectedModel.classList.remove('hidden');
    }
}
<script>
const unavailabletimes=JSONE.parser('{{unavailble_timessafe}}');
disableUnavailabletimes(unavailabletimes);
</script>
function disableUnavailable(unavaTimesilable){
    const selectElement=document.getElementById('id_appointment_time');
    for(let option of selectElement.options){
     if(unavaTimesilable.includes(option.value)){
        option.disabled=true;
     } 
   }
  
}
$(document).ready(function() {

    $(".savedatap").click(function(){
       var csrfToken=$('meta[name="csrf-token"]').attr('content');
      $.ajax({

                  type:"POST",
                  url:"http://" + window.location.host + "/submit_reservation1",
                  data: $(".frm").serialize(),
                  headers:{
                    'X-CSRFToken':csrfToken
                  },
                  beforesend:function() {
                      $(".result").html("در حال ارسال .....");   },
                      

                  success: function(result){
                    console.log(result);
                      if (result=="true"){
                          $(".result").html("ثبت اطلاعات انجام شد ");
                       
                      } 
                       else{
                          $(".result").html("مشکلی  رخ داد  ");
                      }
                     },
                  error:function (e) {
                          $(".result").html("مشکلی در ثبت رخ داد  ");  }

          });

         });
    $(".ok_deletp").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/delet_moshaver",
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



    $("#desktoptype").chainedTo("#datacenter");
    $("#os").chainedTo("#datacenter,#desktoptype");
    $("#bu").chainedTo("#datacenter,#desktoptype,#os");




$(document).ready(function () {
// Checking button status ( wether or not next/previous and
// submit should be displayed )
const checkButtons = (activeStep, stepsCount) => {
    const prevBtn = $("#wizard-prev");
    const nextBtn = $("#wizard-next");
    const submBtn = $("#wizard-subm");

    switch (activeStep / stepsCount) {
        case 0: // First Step
            prevBtn.hide();
            submBtn.hide();
            nextBtn.show();
            break;
        case 1: // Last Step
            nextBtn.hide();
            prevBtn.show();
            submBtn.show();
            break;
        default:
            submBtn.hide();
            prevBtn.show();
            nextBtn.show();
    }
};

// Scrolling the form to the middle of the screen if the form
// is taller than the viewHeight
const scrollWindow = (activeStepHeight, viewHeight) => {
    if (viewHeight < activeStepHeight) {
        $(window).scrollTop($(steps[activeStep]).offset().top - viewHeight / 2);
    }
};

// Setting the wizard body height, this is needed because
// the steps inside of the body have position: absolute
const setWizardHeight = activeStepHeight => {
    $(".wizard-body").height(activeStepHeight);
};

$(function () {
    // Form step counter (little cirecles at the top of the form)
    const wizardSteps = $(".wizard-header .wizard-step");
    // Form steps (actual steps)
    const steps = $(".wizard-body .step");
    // Number of steps (counting from 0)
    const stepsCount = steps.length - 1;
    // Screen Height
    const viewHeight = $(window).height();
    // Current step being shown (counting from 0)
    let activeStep = 0;
    // Height of the current step
    let activeStepHeight = $(steps[activeStep]).height();

    checkButtons(activeStep, stepsCount);
    setWizardHeight(activeStepHeight);

    // Resizing wizard body when the viewport changes
    $(window).resize(function () {
        setWizardHeight($(steps[activeStep]).height());
    });

    // Previous button handler
    $("#wizard-prev").click(() => {
        // Sliding out current step
        $(steps[activeStep]).removeClass("active");
        $(wizardSteps[activeStep]).removeClass("active");

        activeStep--;

        // Sliding in previous Step
        $(steps[activeStep]).removeClass("off").addClass("active");
        $(wizardSteps[activeStep]).addClass("active");

        activeStepHeight = $(steps[activeStep]).height();
        setWizardHeight(activeStepHeight);
        checkButtons(activeStep, stepsCount);
    });

    // Next button handler
    $("#wizard-next").click(() => {
        // Sliding out current step
        $(steps[activeStep]).removeClass("inital").addClass("off").removeClass("active");
        $(wizardSteps[activeStep]).removeClass("active");

        // Next step
        activeStep++;

        // Sliding in next step
        $(steps[activeStep]).addClass("active");
        $(wizardSteps[activeStep]).addClass("active");

        activeStepHeight = $(steps[activeStep]).height();
        setWizardHeight(activeStepHeight);
        checkButtons(activeStep, stepsCount);
    });
});
});


$(document).ready(function(){
    const Stime ="{{consultant.start_time}}";
    const Etime ="{{consultant.end_time}}";
    console.log()

    const $timeselect =$("time");

    let Starttime =new Date('1970-01-01T${Stime}:00');
    let Endtime =new Date('1970-01-01T${Etime}:00');

  
    while (Starttime <=Endtime ){
        const hours=('0'+Starttime.getHours()).slice(-2);
        const minutes=('0'+Starttime.getMinutes()).slice(-2);
        const timeOption='<option value="${hours}:${minutes}">${hours}:${minutes}</option>';
        $timeselect.append(timeOption);
        Starttime.setMinutes(Starttime.getMinutes()+30)

    }


});
