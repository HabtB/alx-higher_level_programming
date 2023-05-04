$(function() {
  $('#toggle_header').on('click', function() {
    var currentClass = $('header').attr('class');
    if (currentClass === 'green') {
      $('header').removeClass('green').addClass('red');
    } else {
      $('header').removeClass('red').addClass('green');
    }
  });
});
