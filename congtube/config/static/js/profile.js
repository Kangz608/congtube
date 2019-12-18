
document.addEventListener('DOMContentLoaded',function(){
    document.getElementById('top').addEventListener('click',function(){
        window.scrollTo({
            top:0,
            left:0,
            behavior:'smooth'
        });
    });

    var orderItem = document.getElementsByClassName('order-list-item');
    for(var i = 0;i<orderItem.length;i++){
        if(i>3){
            orderItem[i].style.display='none';
        }
    }

    document.addEventListener('scroll',toggleOrderItems);


    function toggleOrderItems(){
        var oII = 0;
        while(oII<orderItem.length){
            var nextStep = orderItem[oII+3];
            var prevStep = orderItem[oII-1];
            if(oII!==0&&prevStep.getBoundingClientRect().top<=0){
                nextStep.style.display='block';
            }else if(orderItem[oII].getBoundingClientRect().top>50){
                orderItem.style.display='none';
            };
            oII++;
        }
    }

    document.addEventListener('scroll',function(){
    
        if(window.innerWidth<992){
            if(window.scrollY===0){
            document.getElementById('top').style.display='none';
            for(var i = 0;i<orderItem.length;i++){
                if(i>3){
                    orderItem[i].style.display='none';
                }
            };
            }else{
            document.getElementById('top').style.display='block'
            };
    
        }else{
            document.getElementById('top').style.display='none'
            for(var i = 0;i<orderItem.length;i++){
                orderItem[i].style.display='block';
            };
        }
    });

});
