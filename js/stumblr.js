$("nav li").mouseover(function(event) {
    var id = $(this).id();
    var path = id.substr(7);
    var content = "#content" + path;
    $("article").fadeOut();
    $(content).fadeIn();
});
