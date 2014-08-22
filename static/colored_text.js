text = "pisskidney"
sleep = 500

function randomColoredText(text, parent) {
    parent.innerHTML = ''
    for (i=0; i<text.length; i++) {
        old = parent.innerHTML
        color = (Math.random()*0xFFFFFF<<0).toString(16)
        parent.innerHTML = 
        old + "<span style='color: #" + color + "'>" + text[i] + "</span>"
    }
    parent.innerHTML += ".com"
}

function go() {
    window.setInterval(
        function() {
            randomColoredText(text, document.getElementById("title"))
        },
        sleep
    );
}

go();
