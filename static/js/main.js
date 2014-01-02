var wwg = wwg || {};
wwg.cardgames = wwg.cardgames || {};


wwg.cardgames.init = function(apiRoot) {
    wwg.cardgames.util.log("wwg.cardgames.init");
    var apisToLoad;
    var callback = function() {
        if (--apisToLoad == 0) {
            wwg.cardgames.loadPage();
        }
    }

    apisToLoad = 1; // must match number of calls to gapi.client.load()
    gapi.client.load('cardgames', 'v1', callback, apiRoot);

    // Initialize our image cache
    wwg.cardgames.util.initImages(function() {
        // Set up our UI
        wwg.cardgames.draw.init();
    });
};

wwg.cardgames.loadPage = function() {
    wwg.cardgames.util.log("wwg.cardgames.loadPage");
    wwg.cardgames.listAllGames();
}

wwg.cardgames.createGame = function() {
    wwg.cardgames.util.log("wwg.cardgames.createGame");
    gapi.client.cardgames.game.add().execute(function(resp) {
        if (!resp.code) {
            wwg.cardgames.listAllGames();
        }
    });
};

wwg.cardgames.listAllGames = function() {
    wwg.cardgames.util.log("wwg.cardgames.listAllGames");
    gapi.client.cardgames.game.list.all().execute(function(resp) {
        if (!resp.code) {
            console.log(resp);
            if (resp.items !== undefined) {
                for (var i = 0; i < resp.items.length; i++) {
                    // TODO: implement
                    // var item = resp.items[i];
                    // var element = document.createElement('div');
                    // element.innerHTML = item.server_id + " --> " + " (" + item.lastmodified + ")";
                    // document.getElementById('content').appendChild(element);
                }
            }
        }
    });
};

function init() {
    // var ROOT = 'https://worthwhile-games.appspot.com/_ah/api';
    var ROOT = window.location.protocol + '//' + window.location.host + '/_ah/api';
    wwg.cardgames.init(ROOT);
}

$(window).on('resize orientationChanged', function() {
    wwg.cardgames.draw.init();
});
