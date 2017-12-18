var playlist = [
    'Linoleum',
    'Dog Farts',
    'When I Get Old',
    'Leave The Light On',
    'Pirate\'s Life',
    'I\'m Not A Loser'
];

function print(message) {
    document.write(message);
}

function printList(list) {
    var listHTML = '<ol>';
    for (i = 0; i < list.length; i += 1) {
        listHTML += '<li>' + list[i] + '</li>';
    }
    listHTML += '</ol>';
    print(listHTML);
}

printList(playlist);