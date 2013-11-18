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
    wwg.cardgames.draw.drawMainMenu(canvas);
};

wwg.cardgames.draw.drawMenubar = function(canvas) {
    wwg.cardgames.util.log("wwg.cardgames.draw.drawMenubar");
    var ctx = canvas.getContext('2d');

    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, canvas.width, 50);
    ctx.fillStyle = "#FFF";
    ctx.font = "bold " + (50 * .5) + "px sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText("Card Games", canvas.width / 2, 25, canvas.width);
};

wwg.cardgames.draw.drawBackground = function(canvas) {
    wwg.cardgames.util.log("wwg.cardgames.draw.drawBackground");
    var ctx = canvas.getContext('2d');
    var tableImage = wwg.cardgames.util.getImage("wooden_top");
    ctx.drawImage(tableImage, 0, 0, canvas.width, canvas.height);
};

wwg.cardgames.draw.drawMainMenu = function(canvas) {
    wwg.cardgames.util.log("wwg.cardgames.draw.drawMainMenu");

    wwg.cardgames.draw.drawBackground(canvas);
    wwg.cardgames.draw.drawMenubar(canvas);

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

wwg.cardgames.draw.drawRules = function(canvas) {
    wwg.cardgames.util.log("wwg.cardgames.draw.drawRules");

    // TODO: add back button
    wwg.cardgames.draw.drawBackground(canvas);
    wwg.cardgames.draw.drawMenubar(canvas);

    var textblocks = [
        "The basic game of Crazy Eights is played with a standard deck of 52 cards. Each player will be dealt five cards and the rest of the cards will be put into a draw pile which is placed face down on the playing table. After the cards are dealt, one card will be taken from and placed next to the draw pile face up. This will serve as the discard pile. The game will start with player 1 and continue in a counterclockwise fashion around the table. During each turn a player will either need to play a card from their hand or select one card from the draw pile.",
        "Basic Game Play:",
        "1. If the top card is not an eight then a player must play a card that matches suit or the number of the last card in the discard pile.",
        "2. An eight of any suit may be played at anytime during a players turn. If they choose to play an eight they must declare a suit.",
        "3. If an eight is present on the top of the discard pile then a card of the declared suit or another eight can be played.",
        "4. A draw will serve as a turn if a player cannot play a card.",
        "5. If the first card turned up for the discard pile is an eight, then the suit that is on the eight is the suit that should be played next.",
        "6. Jokers can be played on any card, and any card can be played on a Joker.",
        "The first player to successfully get rid of all of their cards wins the game. If at any point in the game the draw pile is empty, all of the cards from the discard pile except for the top card will be re-shuffled to form a new draw pile."
    ];

    var ctx = canvas.getContext('2d');
    ctx.textAlign = "left";
    ctx.textBaseline = "middle";

    var outerPaddingSide = 25;
    var innerPaddingSide = 10;

    var largeHeight = (canvas.height - 50 - (2 * outerPaddingSide));
    var largeWidth = (canvas.width - (2 * outerPaddingSide));
    var startY = 50 + outerPaddingSide;
    var fontSize = 20;

    // Draw full page rounded box
    ctx.fillStyle = "#FFC90E";
    ctx.strokeStyle = "#000";
    wwg.cardgames.draw.roundRect(ctx, outerPaddingSide, startY, largeWidth, largeHeight, 10, true, true);

    // Draw text blocks
    ctx.fillStyle = "#000";
    ctx.font = "bold " + fontSize + "px sans-serif";

    for (var i = 0; i < textblocks.length; i++) {
        startY = wwg.cardgames.draw.wrapText(ctx, textblocks[i], outerPaddingSide + innerPaddingSide,
            startY + (2 * innerPaddingSide), largeWidth - (2 * innerPaddingSide), fontSize);
        startY += innerPaddingSide;
    }
};

wwg.cardgames.draw.drawGameboard = function(canvas, gamestate) {
    wwg.cardgames.util.log("wwg.cardgames.draw.updateUi");
    var ctx = canvas.getContext('2d');

    wwg.cardgames.draw.drawBackground(canvas);
    wwg.cardgames.draw.drawMenubar(canvas);

    // If we have a game, draw the users and cards
    if (gamestate !== undefined && gamestate !== null) {
        // TODO: draw game state
    }
};

// Drawing Utility functions
wwg.cardgames.draw.wrapText = function(context, text, x, y, maxWidth, lineHeight) {
    var words = text.split(' ');
    var line = '';

    for (var n = 0; n < words.length; n++) {
        var testLine = line + words[n] + ' ';
        var metrics = context.measureText(testLine);
        var testWidth = metrics.width;
        if (testWidth > maxWidth && n > 0) {
            context.fillText(line, x, y);
            line = words[n] + ' ';
            y += lineHeight;
        } else {
            line = testLine;
        }
    }
    context.fillText(line, x, y);

    return y;
}


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
