

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