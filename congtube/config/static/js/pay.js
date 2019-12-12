// $(document).ready(function () {
//     var merchant_uid = 'merchant_' + new Date().getTime();
//     var redirect_url = 'http://localhost:8000/orders/complete';

//     function getProductId() {
//         return $(".order-product-info").data('productId');
//     }

//     function getProductName() {
//         return $(".order-product-info").data('productName');
//     }

//     function getProductPrice() {
//         return $(".order-product-info").data('productPrice');
//     }

//     function requestPay() {
//         var productName = getProductName();
//         var productPrice = getProductPrice();

//         var IMP = window.IMP;
//         IMP.init("imp76531045");
//         IMP.request_pay({
//             // pg: "kakaopay",
//             pg: selectedPG,
//             pay_method: "",
//             merchant_uid: merchant_uid,
//             name: productName,
//             amount: productPrice,
//             m_redirect_url: redirect_url
//         }, function (rsp) {
//             if (rsp.success) {
//                 window.location.href =
//                     redirect_url + '?imp_uid=' + rsp.imp_uid + '&merchant_uid=' + rsp.merchant_uid
//             } else {
//                 console.log("fail")
//             }
//         });
//     }

//     function pay() {
//         $.ajax({
//             url: "/api/orders/",
//             dataType: "json",
//             method: "post",
//             data: {
//                 merchant_uid: merchant_uid,
//                 product_pk: getProductId(),
//                 reciever_name: $('input[name=reciever_name]').val(),
//                 phonenumber: $('input[name=phonenumber]').val(),
//                 email: $('input[name=email]').val(),
//                 message: $('textarea[name=message]').val(),
//                 amount: getProductPrice(),
//             }
//         }).success(function (result) {
//             console.log(result);
//             requestPay();
//         }).error(function (result) {
//             console.log(result);
//         });
//     }
// });


// function requestPay() {
//     var productName = getProductName();
//     var productPrice = getProductPrice();

//     var IMP = window.IMP;
//     IMP.init("imp76531045");
//     IMP.request_pay({
//         // pg: "kakaopay",
//         pg: selectedPG,
//         pay_method: "",
//         merchant_uid: merchant_uid,
//         name: productName,
//         amount: productPrice,
//         m_redirect_url: redirect_url
//     }, function (rsp) {
//         if (rsp.success) {
//             window.location.href =
//                 redirect_url + '?imp_uid=' + rsp.imp_uid + '&merchant_uid=' + rsp.merchant_uid
//         } else {
//             console.log("fail")
//         }
//     });
// }

var selectedPG = null;

function selectPayGate(pg) {
    selectedPG = pg;

    var allPaymentDots = document.getElementsByClassName('product-list__product-item-option-dot-selected');

    for (var dI = 0; dI < allPaymentDots.length; dI++) {
        if (allPaymentDots[dI].id !== 'order_payment_' + pg) {
            allPaymentDots[dI].style.display = 'none';
            continue;
        }
        allPaymentDots[dI].style.display = 'block';
    }
}

function pay() {
    function getProductId() {
        return $(".order-product-info").data('productId');
    }

    function getProductName() {
        return $(".order-product-info").data('productName');
    }

    function getProductPrice() {
        return $(".order-product-info").data('productPrice');
    }

    //주문서 필수 항목 작성 요청
    var orderName = $('#order_input_name');
    var orderTel = $('#order_input_phone_number');
    var orderMail = $('#order_input_email');
    var orderMsg = $('#order_input_content');

    if(!orderName.val()){
        confirm('이름을 입력해주세요.',orderName.focus());
        return;
    }else if(!orderTel.val()){
        confirm('전화번호를 입력해주세요.',orderTel.focus());
        return;
    }else if(!(!isNaN(orderTel.val()))){
        confirm('올바른 전화번호를 입력해주세요.',orderTel.focus());
        return;
    }else if(!orderMail.val()){
        confirm('이메일을 입력해주세요.',orderMail.focus());
        return;
    }else if(!orderMsg.val()){
        confirm('요청사항을 입력해주세요.',orderMsg.focus());
        return;
    }else if (!selectedPG) {
        alert('결제 방법을 선택해주세요.');
        return;
    };

    var merchant_uid = 'merchant_' + new Date().getTime();
    var redirect_url = window.location.origin + "/orders/complete";

    function requestPay() {
        var productName = getProductName();
        var productPrice = getProductPrice();

        var IMP = window.IMP;
        IMP.init("imp76531045");
        IMP.request_pay({
            pg: selectedPG,
            pay_method: "",
            merchant_uid: merchant_uid,
            name: productName,
            amount: productPrice,
            m_redirect_url: redirect_url
        }, function (rsp) {
            if (rsp.success) {
                window.location.href =
                    redirect_url + '?imp_uid=' + rsp.imp_uid + '&merchant_uid=' + rsp.merchant_uid
            } else {
                alert('결제 요청에 실패했습니다.');
            }
        });

    }
    
    $.ajax({
        url: "/api/orders/",
        dataType: "json",
        method: "post",
        data: {
            merchant_uid: merchant_uid,
            product_pk: getProductId(),
            reciever_name: $('input[name=reciever_name]').val(),
            phonenumber: $('input[name=phonenumber]').val(),
            email: $('input[name=email]').val(),
            message: $('textarea[name=message]').val(),
            amount: getProductPrice(),
        }
    }).success(function (result) {
        requestPay();
    }).error(function (result) {
        alert('주문에 실패했습니다.');
    });

}
