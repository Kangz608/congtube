document.addEventListener('DOMContentLoaded',function(){
    let bodyHeight = document.body.clientHeight;
    let windowHeight = window.innerHeight;
    window.setTimeout(footerCheck,150);
    function footerCheck(){
        if(windowHeight>bodyHeight){
            document.getElementById('footer').style.position='absolute';
            document.getElementById('footer').style.bottom='0';
        }else{
            document.getElementById('footer').style.position='initial';
            document.getElementById('footer').style.bottom='initial';
        }
    };
    var oldWidth = window.innerWidth;
    document.addEventListener('resize',function(){
        if(window.innerWidth!=oldWidth){
            window.setTimeout(footerCheck,150);
        }
    });
});
