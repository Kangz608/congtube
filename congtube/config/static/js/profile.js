document.addEventListener('DOMContentLoaded',function(){

    var oldWidth = window.innerWidth;
    var oII = 0;
    var test1 = document.getElementById('paginationContainerM').childNodes;
    var test2 = test1.nodeName;
    var test3 = [];
    if(test2==='A'){
        var test4=0;
        while(test4<test1.length){
            test3.push(test1[test4])
            test4++;
        }
        return;

    }
    console.log(test3)
    var WIH = window.innerHeight;
    var BOH = document.body.offsetHeight;

    if(oldWidth<993){
        toggleBlock();
    }else{
        toggleNone();
    };

    function toggleBlock (){
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

    // function toggleOrderItems(){
    // };

    for(var i=8;i<myPagetml.length;i++){
        myPagetml[i].style.display='none'
    }

    function topScroll(){

        var scrollTop = window.scrollY;

        if(scrollTop==(BOH-WIH)){
            // document.getElementById
            console.log(myPagetml)

        }

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
