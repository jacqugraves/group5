document.getElementById("Submit").onclick = function () {
    var div = document.createElement('div');
       div.style.backgroundColor = "black";
       div.style.position = "absolute";
       div.style.left = "50px";
       div.style.top = "50px";
       div.style.height = "10px";
       div.style.width = "10px";

       document.getElementsByTagName('body')[0].appendChild(div);
};