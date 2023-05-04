$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + languageCode;

    $.getJSON(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
