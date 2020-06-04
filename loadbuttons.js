function setButtons(){
   var elements = document.getElementsByClassName("cb");
   for(var i = 0; i < elements.length; i++){
      elements[i].onclick = function(){};
   }
}