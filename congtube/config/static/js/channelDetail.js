var selectedProductId = null;

function selectProduct(productId) {
  selectedProductId = productId;

  var allProductDots = document.getElementsByClassName('product-list__product-item-option-dot-selected');

  for (var dI = 0; dI < allProductDots.length; dI++) {
    if (allProductDots[dI].id !== 'channel_product_' + productId) {
      allProductDots[dI].style.display = 'none';
      continue;
    }
    allProductDots[dI].style.display = 'block';
  }
}

function redirectToOrder() {

  if (selectedProductId == null) {
    alert('상품을 골라주세요.');
    return;
  }

  const newPathname = location.pathname += 'order?product_id=' + selectedProductId;

  location.href = newPathname;
}

document.addEventListener('DOMContentLoaded', function () {
  var allReviewItems = document.getElementsByClassName('review-item');
  var reviewFlipShowBtn = document.getElementById('review_flip_btn_show');
  var reviewFlipHideBtn = document.getElementById('review_flip_btn_hide');

  if (allReviewItems.length > 3) {
    reviewFlipShowBtn.style.display = 'block';
  }

  for (var rII = 0; rII < allReviewItems.length; rII++) {
    if (rII < 3) {
      allReviewItems[rII].style.display = 'block';
    }else{
      allReviewItems[rII].style.display = 'none';
    }
  }

  reviewFlipShowBtn.addEventListener('click', showReviews);
  reviewFlipHideBtn.addEventListener('click', hideReviews);

  function showReviews() {
    var allReviewItems = document.getElementsByClassName('review-item');
    for (var rII = 0; rII < allReviewItems.length; rII++) {
      allReviewItems[rII].style.display = 'block';
    }

    reviewFlipShowBtn.style.display = 'none';
    reviewFlipHideBtn.style.display = 'block';
    return;
  }

  function hideReviews() {
    var allReviewItems = document.getElementsByClassName('review-item');
    for (var rII = 0; rII < allReviewItems.length; rII++) {
      if (rII >= 3) {
        allReviewItems[rII].style.display = 'none';
      }
    }
    reviewFlipShowBtn.style.display = 'block';
    reviewFlipHideBtn.style.display = 'none';
  }
});


// 반응형 resize할 때 readmore icon view 설정
window.addEventListener('resize',function(){

  var readMore = document.getElementsByClassName('readMore');
  var readMoreMobile = document.querySelectorAll('#fold');

  if(window.innerWidth>992){
    for (var RI = 0; RI<readMore.length;RI++){
      readMore[RI].style.display='none';
    }
  }else{
    for (var RI = 0; RI<readMore.length;RI++){
      for (var RMI = 0; RMI<readMoreMobile.length;RMI++){
        readMoreMobile[RMI].style.display='block';
      }
    }
  }
},true);

// document.addEventListener('DOMContentLoaded', function () {
//   var optionPriceElements = document.getElementsByClassName('product-list__product-item-option-price');

//   for (var eI = 0; eI < optionPriceElements.length; eI++) {
//     var priceInteger = Math.round(optionPriceElements[eI].innerText * 1);

//     optionPriceElements[eI].innerText = priceInteger;
//   }
// });

function flipVolumeChannelDetail(status) {
  if (!status) {
    document.getElementById('channel-detail__volume-on').style.display = 'block';
    document.getElementById('channel-detail__volume-off').style.display = 'none';
  } else {
    document.getElementById('channel-detail__volume-on').style.display = 'none';
    document.getElementById('channel-detail__volume-off').style.display = 'block';
  }
  document.getElementById('channel_detail_video').muted = status;
}

// play on-off bestvideo
window.onload = function(){

  var videoItem = document.getElementsByClassName("bestvideo-item");
  var video = document.getElementsByClassName('bestvideo__image');

  for(var i=0; i<video.length; i++){
    (function(i){
      var playon = video[i].nextElementSibling;
      var playoff = playon.nextElementSibling;

      videoItem[i].addEventListener("click", togglePlayVideo);
      video[i].addEventListener("ended",videoEnded);

      function togglePlayVideo(){ 
        if(video[i].paused){
          playon.style.display = 'none';
          playoff.style.display = 'block';
          video[i].play();
        }else{
          playon.style.display = 'block';
          playoff.style.display = 'none';
          video[i].pause();
        }
      }

      function videoEnded(){
          playon.style.display = 'block';
          playoff.style.display = 'none';
          video[i].currentTime=0;
      }
    })(i);
  };

};

// float purchase

function floatPurchaseOpen(){
    document.getElementById('floating_btn_on').style.display='none';
    document.getElementById('floating_btn_off').style.display='block';
};

function floatPurchaseClose(){
  document.getElementById('floating_btn_on').style.display='block';
  document.getElementById('floating_btn_off').style.display='none';
};

//mobile _ 비디오 이용정책, 환불규정, 리뷰 더보기 버튼 (아코디언)

function readMore(id){
  if(window.innerWidth<993){
    var fold = id.childNodes[1];
    var unfold = id.childNodes[3];

    if(fold.style.display!='none'){

      id.parentNode.className += ' on';
      id.parentNode.parentNode.className += ' on';
      fold.style.display = 'none';
      unfold.style.display = 'block';

    }else{
      id.parentNode.classList.remove('on');
      id.parentNode.parentNode.classList.remove('on');
      fold.style.display = 'block';
      unfold.style.display = 'none';
    }
  }
}

//mobile _ 하단footer 아코디언

function footerMobileFold(id){

var fold = id.childNodes[1];
var unfold = id.childNodes[3];
var address = document.getElementsByTagName('address')[1];

  if(address.style.display!='block'){
    fold.style.display='none';
    unfold.style.display='inline-block';
    address.style.display='block';
  }else{
    fold.style.display='inline-block';
    unfold.style.display='none';
    address.style.display='none';
  }
  
}
