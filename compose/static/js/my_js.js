$('[id*="fav_button_"]').click(function (e) {
  movie_id = event.srcElement.id.replace('fav_button_', '')
  $.ajax({
    type: "GET",
    url: addToFavourites,
    data: {'movie_id': movie_id},
    dataType: 'json',
    success: function (data) {
      if (data['added']){
        alert('Movie has been added to your favourites')
      }else{
        alert("You've already added this movie to favourites")
      }
    }
  });
});
