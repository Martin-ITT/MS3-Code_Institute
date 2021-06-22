$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.carousel').carousel();
  });

  /* footer copyright */
$("#year").text(function () {
  let y = new Date();
  let year = y.getFullYear();
  return year;
});