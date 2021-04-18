$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
});


$(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        "Apple": null,
        "Microsoft": null,
        "Google": 'https://placehold.it/250x250'
      },
    });
  });