var wwg = wwg || {};
wwg.cardgames = wwg.cardgames || {};
wwg.cardgames.draw = wwg.cardgames.draw || {};

wwg.cardgames.draw.init = function() {
    console.log("wwg.cardgames.draw.init");

    // Make the canvas fit the screen
    var canvas = document.getElementById('canvas');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    // Draw the initial state
    wwg.cardgames.draw.updateUi(canvas);
};

wwg.cardgames.draw.updateUi = function(canvas, gamestate) {
    console.log("wwg.cardgames.draw.updateUi");
    var ctx = canvas.getContext('2d');

    // Draw top bar
    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, canvas.width, 50);
    ctx.fillStyle = "#FFF";
    ctx.font = "bold 30px sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "top";
    ctx.fillText("Card Games", canvas.width / 2, 7, canvas.width);

    // Background image
    var tableImage = wwg.cardgames.util.getImage("wooden_top");
    ctx.drawImage(tableImage, 0, 50, canvas.width, canvas.height - 50);

    // If we have a game, draw the users and cards
    if (gamestate !== undefined && gamestate !== null) {
        // TODO: draw game state
    } else {
        ctx.fillStyle = "#FFC90E";
        ctx.strokeStyle = "#000";
        var paddingSide = 100;
        var width = (canvas.width - (2 * paddingSide));
        var height = 100;
        var startY = ((canvas.height - 50) / 2);
        wwg.cardgames.draw.roundRect(ctx, paddingSide, startY, width, height, 10, true, true);

        // Draw text
        ctx.fillStyle = "#000";
        ctx.font = "bold 36px sans-serif";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText("Card Games!", paddingSide + width / 2, startY + height / 2, width);
    }
};


wwg.cardgames.draw.roundRect = function(ctx, x, y, width, height, radius, fill, stroke) {
    console.log("wwg.cardgames.draw.updateUi");

    if (typeof stroke == "undefined") {
        stroke = true;
    }
    if (typeof radius === "undefined") {
        radius = 5;
    }
    ctx.beginPath();
    ctx.moveTo(x + radius, y);
    ctx.lineTo(x + width - radius, y);
    ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
    ctx.lineTo(x + width, y + height - radius);
    ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
    ctx.lineTo(x + radius, y + height);
    ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
    ctx.lineTo(x, y + radius);
    ctx.quadraticCurveTo(x, y, x + radius, y);
    ctx.closePath();
    if (stroke) {
        ctx.stroke();
    }
    if (fill) {
        ctx.fill();
    }
}
