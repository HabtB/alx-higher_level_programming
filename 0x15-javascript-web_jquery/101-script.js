$(document).ready(function() {
  // Add item
  $("#add_item").on("click", function() {
    $(".my_list").append("<li>Item</li>");
  });

  // Remove item
  $("#remove_item").on("click", function() {
    $(".my_list li:last-child").remove();
  });

  // Clear list
  $("#clear_list").on("click", function() {
    $(".my_list").empty();
  });
});
