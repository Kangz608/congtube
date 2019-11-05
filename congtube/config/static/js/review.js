$(document).ready(function () {
    $("#review_submit").click(function () {
        createReview();
        return false;
    });
});


function createReview() {
    const bodyData = {
        order_id: location.pathname.split('/')[2],
        rating: reviewRatingStars,
        message: $('textarea[name=message]').val(),
    };

    $.ajax({
        url: "/api/reviews/",
        dataType: "json",
        method: "post",
        data: {
            order_id: location.pathname.split('/')[2],
            rating: reviewRatingStars,
            message: $('#review_input_content').val(),
        }
    }).success(function (result) {
        window.location.reload();
    }).error(function (result) {
        alert('오류가 발생했습니다.');
        window.location.reload();
    });
}


var reviewRatingStars = 5;

function rateStars(rating) {
    reviewRatingStars = rating;

    var ratingStarNumberElement = document.getElementById('review-create-rating-star-number');

    ratingStarNumberElement.innerText = rating;

    // rSI = ratingStarIndex
    for (var rSI = 1; rSI <= rating; rSI++) {
        var offStar = document.getElementById('order-detail__review-star-' + rSI + '--off');
        var onStar = document.getElementById('order-detail__review-star-' + rSI + '--on');
        offStar.style.display = 'none';
        onStar.style.display = 'block';
    }

    // rSOI = ratingStarOffsetIndex
    for (var rSOI = rating + 1; rSOI <= 5; rSOI++) {
        var offStar = document.getElementById('order-detail__review-star-' + rSOI + '--off');
        var onStar = document.getElementById('order-detail__review-star-' + rSOI + '--on');
        onStar.style.display = 'none';
        offStar.style.display = 'block';
    }
}