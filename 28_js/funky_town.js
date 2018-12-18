/*
Joan Chirinos, Johnny Wong - JoJoVines
SoftDev1 pd08
K28 -- Sequential Progression
2018-12-18
*/

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
