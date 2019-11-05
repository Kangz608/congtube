document.addEventListener('DOMContentLoaded', function () {
  var searchBarForm = document.getElementById('content_search_bar_form');
  var searchBarSubmitImg = document.getElementById('content_search_bar_submit');

  searchBarSubmitImg.addEventListener('click', function () {
    searchBarForm.submit();
  });
});

document.addEventListener('DOMContentLoaded', function () {
  var headerSearchBarForm = document.getElementById('header_search_bar_form');
  var headerSearchBarSubmitImg = document.getElementById('header_search_bar_submit');

  headerSearchBarSubmitImg.addEventListener('click', function () {
    headerSearchBarForm.submit();
  });
});