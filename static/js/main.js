var wwg = wwg || {};
wwg.cardgames = wwg.cardgames || {};


wwg.cardgames.init = function(apiRoot) {
    var apisToLoad;
    var callback = function() {
        if (--apisToLoad == 0) {
            wwg.cardgames.loadPage();
        }
    }

    apisToLoad = 1; // must match number of calls to gapi.client.load()
    gapi.client.load('cardgames', 'v1', callback, apiRoot);
};

wwg.cardgames.loadPage = function() {
    wwg.cardgames.listAllGames();
    wwg.cardgames.enableButtons();
}

wwg.cardgames.enableButtons = function() {
    document.getElementById('create-game').onclick = function() {
        wwg.cardgames.createGame();
    }
};

wwg.cardgames.createGame = function() {
    gapi.client.cardgames.game.add().execute(function(resp) {
        if (!resp.code) {
            wwg.cardgames.listAllGames();
        }
    });
};

wwg.cardgames.listAllGames = function() {
    gapi.client.cardgames.game.list.all().execute(function(resp) {
        if (!resp.code) {
            console.log(resp);
            for (var i = 0; i < resp.items.length; i++) {
                var item = resp.items[i];
                var element = document.createElement('div');
                element.innerHTML = item.server_id + " --> " + " (" + item.lastmodified + ")";
                document.getElementById('content').appendChild(element);
            }
        }
    });
};

function init() {
    // var ROOT = 'https://worthwhile-games.appspot.com/_ah/api';
    var ROOT = window.location.protocol + '//' + window.location.host + '/_ah/api';
    wwg.cardgames.init(ROOT);
}

