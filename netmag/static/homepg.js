

// Get the showmorepub div
var showmpdiv = document.getElementById('showMorepub');

// Get the button that shows more pubposts
var showpubbtn = document.getElementById("shpubBtn");

// Get the showmoreunpub div
var showmunpdiv = document.getElementById('showMoreunpub');

// Get the button that shows more unpubposts
var showunpubbtn = document.getElementById("shunpubBtn");

// When the user clicks on the showmorepubbutton, show more published
showpubbtn.onclick = function() {
    showmpdiv.style.display = "block";
    showpubbtn.style.display = "none";
}


// When the user clicks on the showmoreunpubbutton, show more unpublished
showunpubbtn.onclick = function() {
    showmunpdiv.style.display = "block";
    showunpubbtn.style.display = "none";
}




// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}