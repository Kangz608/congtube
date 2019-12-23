document.addEventListener('DOMContentLoaded',function(){

    // 변수 선언
    var oldWidth = window.innerWidth;
    var WIH = window.innerHeight;
    var orderMCont = document.getElementById('paginationContainerM').childNodes;
    var orderItem = [];
    var status = document.getElementsByClassName('order-list-item__left-order-status');

    // index 변수들
    var oII = 0;    
    var scrollIndex = 0;
    var orderItemIndex =0;
    var status = document.getElementsByClassName('order-list-item__left-order-status');

    // 주문 내역 상태에 따른 css 변경을 위한 addClass
    for(var SI = 0; SI<status.length;SI++){
        if(status[SI].innerHTML==='주문취소'){
            status[SI].classList.add('orderCancled')
        }else if(status[SI].innerHTML==='주문완료'){
            status[SI].classList.add('orderComplete')
        }else if(status[SI].innerHTML==='결제완료'){
            status[SI].classList.add('paymentFinished')
        }
    };

    // 반응형 event
    if(oldWidth<993){
        toggleBlock();
    }else{
        toggleNone();
    };

    // order-list 8개만 보이게 셋팅, scroll event 실행, top버튼 추가 함수
    function toggleBlock (){ 

        while(orderItemIndex<orderMCont.length){
            var orderItemAll = orderMCont[orderItemIndex].nodeName;
            if(orderItemAll=='A'){
                orderItem.push(orderMCont[orderItemIndex]);
            };
            orderItemIndex++;
        };

        scrollIndex = 0;
    
        for(var i = 0 ; i<orderItem.length ;i++){
            if(i>7){
                orderItem[i].style.display='none';
                orderItem[i].classList.remove('order-on');
            };
        };
        
        document.addEventListener('scroll',scrolling);
        document.getElementById('top').style.display='block';
    };


    // scroll event 제거, top버튼 제거 함수
    function toggleNone(){
        document.removeEventListener('scroll',scrolling);
        document.getElementById('top').style.display='none';
    };


    // scroll event 함수
    function scrolling(){

        var scrollTop = window.pageYOffset;
        var BOH = document.body.clientHeight;

        if(scrollTop+WIH===BOH){
            scrollIndex++;
            for(var sII = 0; sII<8;sII++){
                orderItem[scrollIndex*8+sII].style.display='block';
                orderItem[scrollIndex*8+sII].classList.add('order-on');
            }
        };

        if(window.scrollY===0){
            toggleBlock ();
            document.getElementById('top').style.display='none';
        }else{
            document.getElementById('top').style.display='block';
        };
    };

    // top버튼 click시 실행 함수
    function scrollToTop (){
        window.scrollTo({
            top:0,
            behavior:'smooth'
        });        
    };
    
    // resizing 함수
    function myPageResize () {    
        if(window.innerWidth!=oldWidth&&window.innerWidth<993){
            toggleBlock();
        }else{
            toggleNone();
        }
        oldWidth = window.innerWidth;
        return;
    };
    
    document.getElementById('top').addEventListener('click',scrollToTop);
    window.addEventListener('resize',myPageResize);
    
});
