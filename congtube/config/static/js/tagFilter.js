var selectedTagSlug = null;

function selectChannelTag(tagSlug) {
  var allTagElements = document.getElementsByClassName('tags__name-container');
  var allChannelCardElements = document.getElementsByClassName('channel-card__container');

  if (tagSlug === 'all') {
    for (var i = 0; i < allChannelCardElements.length; i++) {
      allChannelCardElements[i].style.display = 'block';
    }

    for (var tI = 0; tI < allTagElements.length; tI++) {
      if (allTagElements[tI].className.split(' ').indexOf('tag_' + tagSlug) !== -1) {
        allTagElements[tI].style.backgroundColor = '#62be51';
        allTagElements[tI].style.color = '#ffffff';
      } else {
        allTagElements[tI].style.backgroundColor = '#f1f1f1';
        allTagElements[tI].style.color = '#aaaaaa';
      }
    }

    selectedTagSlug = tagSlug;
    return;
  }

  // if (selectedTagSlug === tagSlug) {
  //   selectedTagSlug = null;

  //   for (var tI = 0; tI < allTagElements.length; tI++) {
  //     allTagElements[tI].style.backgroundColor = '#f1f1f1';
  //     allTagElements[tI].style.color = '#aaaaaa';
  //   }

  //   for (var i = 0; i < allChannelCardElements.length; i++) {
  //     allChannelCardElements[i].style.display = 'block';
  //   }

  //   return;
  // }

  selectedTagSlug = tagSlug;

  for (var tI = 0; tI < allTagElements.length; tI++) {
    if (allTagElements[tI].className.split(' ').indexOf('tag_' + tagSlug) !== -1) {
      allTagElements[tI].style.backgroundColor = '#62be51';
      allTagElements[tI].style.color = '#ffffff';
    } else {
      allTagElements[tI].style.backgroundColor = '#f1f1f1';
      allTagElements[tI].style.color = '#aaaaaa';
    }
  }

  for (var i = 0; i < allChannelCardElements.length; i++) {
    allChannelCardElements[i].style.display = 'block';
  }

  for (var i = 0; i < allChannelCardElements.length; i++) {
    if (allChannelCardElements[i].className.split(' ').indexOf('channel_tag_' + tagSlug) !== -1) {
      allChannelCardElements[i].style.display = 'block';
    } else {
      allChannelCardElements[i].style.display = 'none';
    }
  }
}