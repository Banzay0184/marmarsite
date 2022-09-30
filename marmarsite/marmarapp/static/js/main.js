$(document).ready(function () {
    $(".owl-carousel").owlCarousel({
        dots: false,
        margin: 10,
        autoplay: true,
        autoplayTimeout: 1800,
        autoplayHoverPause: true,
        loop: true,
        item: 6,
    });
});


$(document).ready(function () {
    $(".users_slider").owlCarousel({
        item: 9,
        dots: false,
        margin: 10,
        autoplay: true,
        nav: true,
        autoplayTimeout: 2000,
        autoplayHoverPause: true,
        loop: true,

    });
});

function openNav() {
    document.getElementById("myNav").style.width = "100%";
}

function closeNav() {
    document.getElementById("myNav").style.width = "0%";
}