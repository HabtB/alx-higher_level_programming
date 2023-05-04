$(document).ready(function () {
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/?lang=${langCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  });

  $('#language_code').keypress(function (e) {
    if (e.keyCode == 13 || e.which == 13) {
      $('#btn_translate').click();
      return false;
    }
  });
});

