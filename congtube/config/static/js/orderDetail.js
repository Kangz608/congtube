// document.addEventListener('DOMContentLoaded', function () {
//   var reviewProductInfoPriceCong = document.getElementById('review-product-info__price-cong');
//   var priceInteger = Math.round(reviewProductInfoPriceCong.innerText * 1);

//   reviewProductInfoPriceCong.innerText = priceInteger;
// });

function copyToClipboard(url) {
  var t = document.createElement("textarea");
  t.style.opacity = 0;
  t.style.height = 0;
  t.style.width = 0;
  t.style.border = 'none';
  t.style.position = 'absolute';
  t.style.bottom = 0;

  document.body.appendChild(t);
  t.value = url;
  t.select();
  t.setSelectionRange(0, 99999);
  document.execCommand('copy');
  document.body.removeChild(t);

  alert('동영상 주소가 클립보드에 복사되었습니다.');
}

function flipVolumeOrderDetail(status) {
  if (!status) {
    document.getElementById('order-detail__volume-on').style.display = 'none';
    document.getElementById('order-detail__volume-off').style.display = 'block';
  } else {
    document.getElementById('order-detail__volume-on').style.display = 'block';
    document.getElementById('order-detail__volume-off').style.display = 'none';
  }
  document.getElementById('order_detail_video').muted = status;
}