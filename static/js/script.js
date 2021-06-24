$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
  });

  /* footer copyright */
$("#year").text(function () {
  let y = new Date();
  let year = y.getFullYear();
  return year;
});