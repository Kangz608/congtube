document.addEventListener('DOMContentLoaded',function(){
    let bodyHeight = document.body.clientHeight;
    let windowHeight = window.innerHeight;
    if(windowHeight>bodyHeight){
        document.getElementById('footer').style.position='absolute';
        document.getElementById('footer').style.bottom='0';
    }else{
        document.getElementById('footer').style.position='initial';
        document.getElementById('footer').style.bottom='initial';
    }
})