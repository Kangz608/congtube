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