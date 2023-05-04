""" Use jQuery's shorthand AJAX method to fetch the movie data """
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  var movieTitles = data.results.map(function(movie) {
    return movie.title;
  });

  var $listMovies = $('#list_movies');

  movieTitles.forEach(function(title) {
    var $li = $('<li>').text(title);
    $listMovies.append($li);
  });
});

