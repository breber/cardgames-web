var wwg = wwg || {};
wwg.cardgames = wwg.cardgames || {};
wwg.cardgames.util = wwg.cardgames.util || {};

wwg.cardgames.util.initImages = function(callback) {
    var images = {};
    images['wooden_top'] = '/static/img/wooden_top.jpg';
    images['back_blue_4'] = '/static/img/cards/back_blue_4.png';
    images['clubs_2'] = '/static/img/cards/clubs_2.png';
    images['clubs_3'] = '/static/img/cards/clubs_3.png';
    images['clubs_4'] = '/static/img/cards/clubs_4.png';
    images['clubs_5'] = '/static/img/cards/clubs_5.png';
    images['clubs_6'] = '/static/img/cards/clubs_6.png';
    images['clubs_7'] = '/static/img/cards/clubs_7.png';
    images['clubs_8'] = '/static/img/cards/clubs_8.png';
    images['clubs_9'] = '/static/img/cards/clubs_9.png';
    images['clubs_10'] = '/static/img/cards/clubs_10.png';
    images['clubs_a'] = '/static/img/cards/clubs_a.png';
    images['clubs_j'] = '/static/img/cards/clubs_j.png';
    images['clubs_q'] = '/static/img/cards/clubs_q.png';
    images['clubs_k'] = '/static/img/cards/clubs_k.png';
    images['diamonds_2'] = '/static/img/cards/diamonds_2.png';
    images['diamonds_3'] = '/static/img/cards/diamonds_3.png';
    images['diamonds_4'] = '/static/img/cards/diamonds_4.png';
    images['diamonds_5'] = '/static/img/cards/diamonds_5.png';
    images['diamonds_6'] = '/static/img/cards/diamonds_6.png';
    images['diamonds_7'] = '/static/img/cards/diamonds_7.png';
    images['diamonds_8'] = '/static/img/cards/diamonds_8.png';
    images['diamonds_9'] = '/static/img/cards/diamonds_9.png';
    images['diamonds_10'] = '/static/img/cards/diamonds_10.png';
    images['diamonds_a'] = '/static/img/cards/diamonds_a.png';
    images['diamonds_j'] = '/static/img/cards/diamonds_j.png';
    images['diamonds_q'] = '/static/img/cards/diamonds_q.png';
    images['diamonds_k'] = '/static/img/cards/diamonds_k.png';
    images['hearts_2'] = '/static/img/cards/hearts_2.png';
    images['hearts_3'] = '/static/img/cards/hearts_3.png';
    images['hearts_4'] = '/static/img/cards/hearts_4.png';
    images['hearts_5'] = '/static/img/cards/hearts_5.png';
    images['hearts_6'] = '/static/img/cards/hearts_6.png';
    images['hearts_7'] = '/static/img/cards/hearts_7.png';
    images['hearts_8'] = '/static/img/cards/hearts_8.png';
    images['hearts_9'] = '/static/img/cards/hearts_9.png';
    images['hearts_10'] = '/static/img/cards/hearts_10.png';
    images['hearts_a'] = '/static/img/cards/hearts_a.png';
    images['hearts_j'] = '/static/img/cards/hearts_j.png';
    images['hearts_q'] = '/static/img/cards/hearts_q.png';
    images['hearts_k'] = '/static/img/cards/hearts_k.png';
    images['spades_2'] = '/static/img/cards/spades_2.png';
    images['spades_3'] = '/static/img/cards/spades_3.png';
    images['spades_4'] = '/static/img/cards/spades_4.png';
    images['spades_5'] = '/static/img/cards/spades_5.png';
    images['spades_6'] = '/static/img/cards/spades_6.png';
    images['spades_7'] = '/static/img/cards/spades_7.png';
    images['spades_8'] = '/static/img/cards/spades_8.png';
    images['spades_9'] = '/static/img/cards/spades_9.png';
    images['spades_10'] = '/static/img/cards/spades_10.png';
    images['spades_a'] = '/static/img/cards/spades_a.png';
    images['spades_j'] = '/static/img/cards/spades_j.png';
    images['spades_q'] = '/static/img/cards/spades_q.png';
    images['spades_k'] = '/static/img/cards/spades_k.png';
    images['joker_b'] = '/static/img/cards/joker_b.png';
    images['joker_r'] = '/static/img/cards/joker_r.png';

    wwg.cardgames.util.loadImages(images, function(images) {
       wwg.cardgames.util._images = images;
       callback();
    });
};

wwg.cardgames.util.getImage = function(name) {
    if (typeof wwg.cardgames.util._images == "undefined") {
        return undefined;
    }

    return wwg.cardgames.util._images[name];
}

wwg.cardgames.util.loadImages = function(sources, callback) {
    var images = {};
    var loadedImages = 0;
    var numImages = 0;

    // get num of sources
    for (var src in sources) {
        numImages++;
    }
    for (var src in sources) {
        images[src] = new Image();
        images[src].onload = function() {
            if (++loadedImages >= numImages) {
              callback(images);
            }
        };
        images[src].src = sources[src];
    }
};
