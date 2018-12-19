/*
Joan Chirinos, Derek Song - JavaSkrrt
SoftDev1 pd08
K28 -- Sequential Progression
2018-12-18
*/

//fxns

var fibonacci = (n) => {
    if (n < 2) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
};

var gcd = (a, b) => {
    if (a < b) {
        var temp = a;
        a = b;
        b = temp;
    }

    var r = a % b;
    if (r == 0) return b;
    else return gcd(b, r);
};

var studentList = ['Joan', 'Johnny', 'a-aron', 'maf', 'brown', 'bni', 'k'];

var randomStudent = () => {
    return studentList[Math.floor(Math.random() * studentList.length)];
};

// display

var display_fib = () => {
    var results = fibonacci(5);
    console.log(results);
    document.getElementById('fib_results').innerHTML = results;
};

var display_gcd = () => {
    var results = gcd(15, 9);
    console.log(results);
    document.getElementById('gcd_results').innerHTML = results;
};

var display_rs = () => {
    var results = randomStudent();
    console.log(results);
    document.getElementById('rs_results').innerHTML = results;
};

//eventListener

var fib5 = document.getElementById('fib5');
fib5.addEventListener('click', display_fib);

var gcd159 = document.getElementById('gcd159');
gcd159.addEventListener('click', display_gcd);

var rs = document.getElementById('randomstudent');
rs.addEventListener('click', display_rs);
