var i = 0;
var elts = document.getElementsByTagName('li');
var next = function(e){
    elts[i % elts.length].classList.toggle('red');
    i++;
    elts[i % elts.length].classList.toggle('red');
}

var foo = document.getElementById('blah');
foo.addEventListener('click',next);

