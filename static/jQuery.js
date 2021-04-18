$(document).ready(function() {
  $(".header-icon").click(function(){
    $(this).toggleClass("active");
    $(".header-title h1").toggleClass("active");
    $(".navigation-panel").toggleClass("active");
    $(".content-items").toggleClass("active");
    $(".content-space").toggleClass("active");
    $(".header-icon i").toggleClass("fa-times");
  });
});
