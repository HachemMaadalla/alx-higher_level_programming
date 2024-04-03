let lang = $('html').attr('lang');
if (typeof lang === typeof undefined || lang === false) {
  lang = 'en';
}
$.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
  $('DIV#hello').text(data.hello);
});
