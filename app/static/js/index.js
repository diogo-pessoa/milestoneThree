$(document).ready(function () {
    //Enable Sidebar
    $(".sidenav").sidenav({edge: "right"});
    //Enable tabs
    $('.tabs').tabs();

    $('input.autocomplete').autocomplete({
      data: {
        "Apple": null,
        "Microsoft": null,
        "Google": 'https://placehold.it/250x250'
      },
    });
});