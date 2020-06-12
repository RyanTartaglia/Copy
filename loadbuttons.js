function copy(that){
   var inp =document.createElement('input');
   document.body.appendChild(inp);
   inp.value =that.textContent;
   inp.select();
   document.execCommand('copy',false);
   inp.remove();
}

window.onload = function() {
    var anchors = document.getElementsByClassName("cb");
    for(var i = 0; i < anchors.length; i++) {
        var anchor = anchors[i];
        anchor.onclick = function() {
            copy(this);
        };
    }
};