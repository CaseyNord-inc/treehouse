var playlist = [
    ['Linoleum', 'NOFX'],
    ['Dog Farts', 'Dayglo Abortions'],
    ['When I Get Old', 'The Descendents'],
    ['Leave The Light On', 'Lagwagon'],
    ['Pirate\'s Life', 'The Vandals'],
    ['I\'m Not A Loser', 'The Descendents']
];

function print(message) {
    document.write(message);
}

function printSongs(songs) {
    var listHTML = '<ol>';
    for (i = 0; i < songs.length; i += 1) {
        listHTML += '<li>' + songs[i][0] + ' by ' + songs[i][1] + '</li>';
    }
    listHTML += '</ol>';
    print(listHTML);
}

printSongs(playlist);