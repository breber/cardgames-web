function init() {
    console.log("Init main");

    var ROOT = 'https://worthwhile-games.appspot.com/_ah/api';
    gapi.client.load('cardgames', 'v1', function() {
        // Get the list of previous scores
        console.log(gapi.client.cardgames);
        gapi.client.cardgames.game.list.all().execute(function(resp) {
            console.log(resp);
        });
    }, ROOT);
}

