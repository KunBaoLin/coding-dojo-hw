console.log("page loaded...");


var count = [9,12,9];
var countElement = [
    document.querySelector("#count1"),
    document.querySelector("#count2"),
    document.querySelector("#count3")
];


function add1(id){
    count[id]++;
    countElement[id].innerHTML = count[id] + " Like(s)";
    console.log("it works");
}
