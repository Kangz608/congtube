// var selectedPG = null;

// function selectPayGate(pg) {
//   console.log('pg: ', pg);
//   selectedPG = pg;

//   var allPaymentDots = document.getElementsByClassName('product-list__product-item-option-dot-selected');

//   for (var dI = 0; dI < allPaymentDots.length; dI++) {
//     if (allPaymentDots[dI].id !== 'order_payment_' + pg) {
//       allPaymentDots[dI].style.display = 'none';
//       continue;
//     }
//     allPaymentDots[dI].style.display = 'block';
//   }
// }

// function redirectToOrder() {
//   console.log('selectedProductId: ', selectedProductId);

//   if (selectedProductId == null) {
//     alert('상품을 골라주세요.');
//     return;
//   }

//   const newPathname = location.pathname += 'order?product_id=' + selectedProductId;

//   location.href = newPathname;
// }