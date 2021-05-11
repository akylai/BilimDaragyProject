$(document).ready(function () {
    $(".pages").click(function (event) {
        $(".pages").toggleClass("active");
        $("body").toggleClass("lock");
    });
});
