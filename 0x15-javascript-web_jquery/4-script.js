$('DIV#toggle_header').click(function () {
  const cls = $('header').attr('class');
  if (cls === 'green') {
    $('header').removeClass('green');
    $('header').addClass('red');
  } else {
    $('header').removeClass('red');
    $('header').addClass('green');
  }
});
