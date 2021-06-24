$(document).ready(function(){
    /* mobile navbar */
    $('.sidenav').sidenav();
    /* error message */
    $('.collapsible').collapsible();
  });

  /* footer copyright */
$("#year").text(function () {
  let y = new Date();
  let year = y.getFullYear();
  return year;
});