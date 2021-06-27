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

/* back to top btn */
/* https://www.w3schools.com/howto/howto_js_scroll_to_top.asp */
var mybutton = document.getElementById("top-btn");

window.onscroll = function() {scrollFunction();};

function scrollFunction() {
  if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}