/*
Joan Chirinos, Johnny Wong - JoJoVines
SoftDev1 pd08
K30 -- Sequential Progression III: Season of the Witch
2018-12-21
*/

// Lo, what is this? Could it be a VALUE-ADDED-KEY2SUCCESS?!?!

// PHASE III

var changeHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = this.innerHTML;
};

var removeItem = function(e) {
    this.remove();
};

var lis = document.getElementsByTagName("li");

for(var i=0; i < lis.length; i++) {
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', function(e){
      document.getElementById("h").innerHTML = "Hello World!";
    });
    lis[i].addEventListener('click', removeItem);
};


var addItem = function(e) {
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    item.addEventListener('mouseover', changeHeading);
    item.addEventListener('mouseout', function(e){
      document.getElementById("h").innerHTML = "Hello World!";
    });
    item.addEventListener('click', removeItem);
    list.appendChild(item);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

// PHASE IV

var fib = function(n) {
    if(n < 2){
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
};


var addFib = function(e){
    console.log(e);
    var fibList = document.getElementById("fiblist");
    var list = fiblist.getElementsByTagName("li");
    console.log(list.length);
    var item = document.createElement("li");
    var fibVal = fib(list.length);
    item.innerHTML = fibVal;
    fibList.appendChild(item)
};

// Fibonacci function with Dynamic Programming
var fib2 = (n) => {
    // store first 2 fib nums
    var fibSeq = [0, 1];
    if(n < 2) return (fibSeq[n]);

    // swap first or second val of fibSeq with summation of prev two values
    var inc = 2;
    while(inc <= n){
        fibSeq[inc % 2] = fibSeq[(inc + 1) % 2] + fibSeq[inc % 2];
        inc++;
    }
    return fibSeq[(inc - 1) % 2];
};


var addFib2 = function(e){
    console.log(e);
    // find fiblist
    var fibList = document.getElementById("fiblist");
    // get list of children under fibList
    var list = fiblist.getElementsByTagName("li");
    console.log(list.length);
    var item = document.createElement("li");
    var fibVal = fib2(list.length);
    item.innerHTML = fibVal;
    fibList.appendChild(item)
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
