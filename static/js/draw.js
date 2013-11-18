var wwg = wwg || {};
wwg.cardgames = wwg.cardgames || {};
wwg.cardgames.draw = wwg.cardgames.draw || {};

wwg.cardgames.draw.init = function() {
    wwg.cardgames.util.log("wwg.cardgames.draw.init");

    // Make the canvas fit the screen
    var canvas = document.getElementById('canvas');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    // Draw the initial state
    wwg.cardgames.draw.updateUi(canvas);
};

wwg.cardgames.draw.updateUi = function(canvas, gamestate) {
    wwg.cardgames.util.log("wwg.cardgames.draw.updateUi");
    var ctx = canvas.getContext('2d');

    // Draw top bar
    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, canvas.width, 50);
    ctx.fillStyle = "#FFF";
    ctx.font = "bold " + (50 * .5) + "px sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText("Card Games", canvas.width / 2, 25, canvas.width);

    // Background image
    var tableImage = wwg.cardgames.util.getImage("wooden_top");
    ctx.drawImage(tableImage, 0, 50, canvas.width, canvas.height - 50);

    // If we have a game, draw the users and cards
    if (gamestate !== undefined && gamestate !== null) {
        // TODO: draw game state
    } else {
        wwg.cardgames.draw.drawMainMenu(canvas);
    }
};

wwg.cardgames.draw.drawMainMenu = function(canvas) {
    wwg.cardgames.util.log("wwg.cardgames.draw.drawMainMenu");

    var ctx = canvas.getContext('2d');
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    var paddingSide = 100;
    var paddingSide2 = 150;

    var bigButtonRatio = .166;
    var smallButtonRatio = .1;

    var largeHeight = (canvas.height * bigButtonRatio);
    var smallHeight = (canvas.height * smallButtonRatio);
    var largeWidth = (canvas.width - (2 * paddingSide));
    var smallWidth = (canvas.width - (2 * paddingSide2));

    var totalHeight = largeHeight + 10 + smallHeight + 10 + smallHeight;
    var startY = (canvas.height - totalHeight) / 2;

    // Create Game button
    ctx.fillStyle = "#FFC90E";
    ctx.strokeStyle = "#000";
    wwg.cardgames.draw.roundRect(ctx, paddingSide, startY, largeWidth, largeHeight, 10, true, true);
    ctx.fillStyle = "#000";
    ctx.font = "bold " + (largeHeight * .5) + "px sans-serif";
    ctx.fillText("Create Game", paddingSide + largeWidth / 2, startY + largeHeight / 2, largeWidth);
    startY += largeHeight + 10;


    // Join Game button
    ctx.fillStyle = "#FFC90E";
    ctx.strokeStyle = "#000";
    wwg.cardgames.draw.roundRect(ctx, paddingSide2, startY, smallWidth, smallHeight, 10, true, true);
    ctx.fillStyle = "#000";
    ctx.font = "bold " + (smallHeight * .5) + "px sans-serif";
    ctx.fillText("Join Game", paddingSide2 + smallWidth / 2, startY + smallHeight / 2, smallWidth);
    startY += smallHeight + 10;


    // Rules button
    ctx.fillStyle = "#FFC90E";
    ctx.strokeStyle = "#000";
    wwg.cardgames.draw.roundRect(ctx, paddingSide2, startY, smallWidth, smallHeight, 10, true, true);
    ctx.fillStyle = "#000";
    ctx.font = "bold " + (smallHeight * .5) + "px sans-serif";
    ctx.fillText("Rules", paddingSide2 + smallWidth / 2, startY + smallHeight / 2, smallWidth);
};

wwg.cardgames.draw.roundRect = function(ctx, x, y, width, height, radius, fill, stroke) {
    wwg.cardgames.util.log("wwg.cardgames.draw.roundRect");

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
