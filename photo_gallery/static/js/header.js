//매뉴가 슬라이더 그라디언트에 있을 때, 그림자 제거로 그라디언트와 일체화.
$(document).ready(function () {
    $('nav').addClass('no-shadow');
});

$(window).on('scroll', function () {
    if ($(window).scrollTop() > 10) {
        $('nav').removeClass('no-shadow');
    } else {
        $('nav').addClass('no-shadow');
    }
});