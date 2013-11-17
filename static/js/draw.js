var wwg = wwg || {};
wwg.cardgames = wwg.cardgames || {};
wwg.cardgames.draw = wwg.cardgames.draw || {};

wwg.cardgames.draw.init = function() {
    console.log("wwg.cardgames.draw.init");

    // Make the canvas fit the screen
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight - 10;

    // Background image
    var table = new Image();
    table.src = "/static/img/wooden_top.jpg";
    table.onload = function() {
        context.drawImage(table, 0, 0, canvas.width, canvas.height);
    };
};
