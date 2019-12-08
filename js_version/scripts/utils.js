// Copy text to clipboard
// From https://stackoverflow.com/a/30810322
function copyToClipboard(text) {
    let textArea = document.createElement('textarea');

    // Place in top-left corner of screen regardless of scroll position.
    textArea.style.position = 'fixed';
    textArea.style.top = 0;
    textArea.style.left = 0;

    // Ensure it has a small width and height. Setting to 1px / 1em
    // doesn't work as this gives a negative w/h on some browsers.
    textArea.style.width = '2em';
    textArea.style.height = '2em';

    // We don't need padding, reducing the size if it does flash render.
    textArea.style.padding = 0;

    // Clean up any borders.
    textArea.style.border = 'none';
    textArea.style.outline = 'none';
    textArea.style.boxShadow = 'none';

    // Avoid flash of white box if rendered for any reason.
    textArea.style.background = 'transparent';


    textArea.value = text;

    document.body.appendChild(textArea);

    textArea.select();

    try {
        let successful = document.execCommand('copy');
        let msg = successful ? 'successful' : 'unsuccessful';
        console.log('Copying text command was ' + msg);
    } catch (err) {
        console.log('Unable to copy');
    }

    document.body.removeChild(textArea);
}

// Count occurance of each state
function countStates() {
    let states = [0, 0, 0, 0];
    let total = 0;
    for (let i = 0; i < entities.length; i++) {
        states[entities[i].state]++;
        total++;
    }

    return [states, total];
}

// Check if coordinate is inside a circle
function inCircle(x, y, cx, cy, r) {
    return sq(x - cx) + sq(y - cy) < sq(r);
}
