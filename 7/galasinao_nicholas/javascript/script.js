var button = document.getElementById("c");
button.addEventListener("click", cycle);

var cycle = function(c){
    console.log(c);
    var list = document.querySelectorAll("li");
    var i = 0;
    if(i == 0)
	list[i].classList.add("green");
    else{
	list[i%5-1].classList.toggle("green");
	list[i%5].classList.toggle("green");
    } 
    i++;
	
}