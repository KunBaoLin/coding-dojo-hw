console.log("page loaded...");


var count = 9;
var countElement = document.querySelector("#counts");

function add1(){
    count ++;
    countElement.innerText = count + " Likes";
    console.log(count);
    console.log("it works")
}