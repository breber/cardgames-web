var wwg = wwg || {};
wwg.cardgames = wwg.cardgames || {};
wwg.cardgames.util = wwg.cardgames.util || {};

wwg.cardgames.util.log = function(message) {
    console.log(message);
}

wwg.cardgames.util.breadcrumb = function(breadcrumb) {
    window.location.hash = breadcrumb;
}
