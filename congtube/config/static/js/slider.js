// $(document).ready(function () {
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, { edge: 'right' });
});
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.carousel');

    var instances = M.Carousel.init(elems, {
        fullWidth: true,
        indicators: true,
    });
});


// slide-banner
document.addEventListener('DOMContentLoaded', function() {
    document.getElementsByClassName('indicators')[0].setAttribute('id','indicator');
    var banner = document.getElementsByClassName('carousel-item');
    var bannerIndex =0;
    var bannerContents = document.getElementsByClassName('bannerConts');
    var g = document.getElementById('indicator');
    var x1 = null;
    var y = null;

    // bannertitle을 이용해 컨텐츠를 나타내보자.
    while(bannerIndex<banner.length){
        if(banner[bannerIndex].className = 'carousel-item active'){
            x1 = document.getElementsByClassName('conts')[bannerIndex].innerHTML;
            y= x1.replace(/&lt;|&gt;/g,function(tst){
                switch(tst){
                    case '&lt;' : return '<';
                    case '&gt;' : return  '>';
                };
            });
            bannerContents[bannerIndex].innerHTML=y;
        }else{
            continue;
        }
        bannerIndex ++;
    };

    //indicator을 사용할 때 배너 컨텐츠를 바꿔보자
     for (var i = 0; i < g.children.length; i++)
        {
            (function(index){
                g.children[i].onclick = function(){
                    x1= document.getElementsByClassName('conts')[index].innerHTML;
                    y = x1.replace(/&lt;|&gt;/g,function(tst){
                        switch(tst){
                            case '&lt;' : return '<';
                            case '&gt;' : return  '>';
                        };
                    });
                    bannerContents[index].innerHTML=y;
                };
            })(i);
        
        };

});


//window resize시 img변경 (반응형)
var bannerRes = document.getElementsByClassName('carousel-item');

window.addEventListener('resize',function(){
    if(window.innerWidth<993){
        bannerResize();
    }else{
        bannerOriginal();
    }
},false);

window.addEventListener('DOMContentLoaded',function(){
    if(window.innerWidth<993){
        bannerResize();
    }else{
        bannerOriginal();
    }
})

function bannerResize(){
    for(var i =0; i<bannerRes.length;i++){
        var oldSrc = bannerRes[i].childNodes[1].getAttribute('src');
        var newSrc = oldSrc.replace(/.png|_m.png/g,'_m.png');
        bannerRes[i].childNodes[1].setAttribute('src',newSrc);
    }
};

function bannerOriginal(){
    for(var i =0; i<bannerRes.length;i++){
        var oldSrc = bannerRes[i].childNodes[1].getAttribute('src');
        var newSrc = oldSrc.replace(/.png|_m.png/g,'.png');
        bannerRes[i].childNodes[1].setAttribute('src',newSrc);
    }
}




// var indicator = document.getElementsByClassName('indicator');
// var indicatorIndex = 0;
// while(indicatorIndex<indicator.length){
//     indicator[indicatorIndex]
//     indicatorIndex++;
// }



// // 윈도우 load시 첫번째 banner contents만 보이게
// window.addEventListener('DOMContentLoaded',function(){

//     var elemsItems = document.querySelectorAll('.carousel-item');
//     var activeElemsItem = document.getElementsByClassName('carousel-item active');
//     var activeSlideContents = document.getElementById('banner-conts');
//     var slideContents = document.getElementsByClassName('banner-cont-container');
//     var slideConts = document.getElementsByClassName('banner-contents-wrap')[0].childNodes;
//     var activeConts = [];

//     var i = 0;
//     while(i<slideConts.length)
//     {
//         if(slideConts[i].tagName=='DIV'){
//             activeConts.push(slideConts[i].innerHTML)
//         }
//         i++;
//     }

//     var sI=0;
//     while (sI<elemsItems.length){  
//         if(elemsItems[sI].className=='carousel-item active'){
//             activeSlideContents.innerHTML = activeConts[sI];
//             activeSlideContents.style.display='block';
//             activeSlideContents.className += 'banner-'+sI+'-wrap'
//             console.log(activeSlideContents)
//             // activeSlideContents.innerHTML = 'activeConts[sI].innerHTML';
//         };
//         sI++;
//     }
    
//     // indicator 선택시 해당 banner contents 보이게

//     var bannerIndicator = document.getElementsByClassName('indicator-item');
//     var activeIndicator = document.getElementsByClassName('indicator-item active');

//         var iI=0;
        
//         function toggleBannerShow(){ 

//             activeSlideContents.innerHTML = '';
//             while (iI<bannerIndicator.length){  
//                 if(bannerIndicator[iI].className=='indicator-item active'){
//                     activeSlideContents.innerHTML = activeConts[iI];
//                     activeSlideContents.style.display='block';
//                     activeSlideContents.className += 'banner-'+iI+'-wrap'
//                     // activeSlideContents.innerHTML = 'activeConts[iI].innerHTML';
//                 };
//                 iI++;
//             }
//         }
// });

// });

