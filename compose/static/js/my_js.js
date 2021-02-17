$("#sending-button").click(function (e) {
  $.ajax({
    type: "GET",
    url: addToFavourites,
    data: {'user_name': 'test'},
    dataType: 'json',
    success: function (data) {
        alert('dodano film do ulubionych')
    }
  });
});
