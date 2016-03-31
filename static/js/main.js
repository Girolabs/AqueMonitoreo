;(function($) {
	$.fn.extend({
    animateCss: function (animationName) {
        var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
        $(this).addClass('animated ' + animationName).one(animationEnd, function() {
            $(this).removeClass('animated ' + animationName);
        });
    }
});

$('#main').animateCss('bounceInLeft');
$('#titulo').animateCss('bounceInLeft');
$('#menuPrincipal').animateCss('bounceInLeft');
})(jQuery);