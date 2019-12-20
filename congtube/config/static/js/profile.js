document.addEventListener('DOMContentLoaded',function(){

    var oldWidth = window.innerWidth;
    var oII = 0;    
    var WIH = window.innerHeight;
    var BOH = document.body.offsetHeight;
    var orderMCont = document.getElementById('paginationContainerM').childNodes;
    var orderItem = [];
    var orderItemIndex =0;

    if(oldWidth<993){
        toggleBlock();
    }else{
        toggleNone();
    };

    function toggleBlock (){       
    
        while(orderItemIndex<orderMCont.length){
            var orderItemAll = orderMCont[orderItemIndex].nodeName;
            if(orderItemAll=='A'){
                orderItem.push(orderMCont[orderItemIndex]);
            };
            orderItemIndex++;
        };
    
        for(var i = 0 ; i<orderItem.length ;i++){
            if(i>7){
                orderItem[i].style.height='0';
            };
        };
        
        document.addEventListener('scroll',topScroll);
        document.getElementById('top').style.display='block';
    };

    function toggleNone(){
        document.removeEventListener('scroll',topScroll);
        document.getElementById('top').style.display='none';
    };

    function myPageResize(){        
        if(window.innerWidth!==oldWidth&&window.innerwidth<993){
            toggleBlock();
        }else{
            toggleNone();
        }
        oldWidth = window.innerWidth;
        return;
    };


    function topScroll(){
        var scrollTop = window.scrollY;
        
        console.log(scrollTop,BOH,WIH)
        if(scrollTop==(BOH-WIH)){
            
            alert('?')

        };

        if(window.scrollY===0){
            document.getElementById('top').style.display='none';
        }else{
            document.getElementById('top').style.display='block';
        };
    };

    function scrollToTop (){
        window.scrollTo({
            top:0,
            left:0,
            behavior:'smooth'
        });
    };

    
    document.getElementById('top').addEventListener('click',scrollToTop);
    document.addEventListener('resize',myPageResize);
    
    

});
