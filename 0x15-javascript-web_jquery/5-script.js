$(function() {
  $('#add_item').on('click', function() {
    var newItem = $('<li>Item</li>');
    $('.my_list').append(newItem);
  });
});
