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


