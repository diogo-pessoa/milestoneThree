$(document).ready(function () {
    //Enable Sidebar
    $(".sidenav").sidenav({edge: "right"});
    //Enable tabs
    $('.tabs').tabs();
    // enable dropdown
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();
    // enable collapsible
    $('.collapsible').collapsible();
});