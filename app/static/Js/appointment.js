
//جدیدهزی
$(document).addEventListener('DOmContentLoaded',function(){
    function loadAvailableTime(consultantid,date){
        consol.log(dateinput.value);
        const url='/api/availablt_times/${consultantid}/${date}/';
        fetch(url,{
            method:GET,
            headers:{
             'X-Requested-with':'XMLHttpRequest'
                    
                }
            })
            .then(response=> response.jsone())
            .then(data=>{
               consol.log(data);
               const timesList=document.getElementById('availablt-times-list');

               timesList.innerHTML='';  
               if(data.availablt_times.length>0){
                data.availablt_times.forEach(time=>{
                    const li=document.createElement('li');
                    li.textContent=time;
                    timesList.appendChild(li);
                });
      }else{
        const li=document.creatElement('li');
        li.textContent='';
        timesList.appendChild(li);

      }
    })
    .catch(error=>{console.error('Error.',error);
    });
}
    const checkTimeButton=document.getElementById('check-times-button');
    const consultantid=document.getElementById('consultant-id').value;
    const dateinput=document.getElementById('date-input');
    checkTimeButton.addEventListener('click',function(){
        const date=dateinput.value;
        loadAvailableTime(consultantid,date);
    }); 
});
