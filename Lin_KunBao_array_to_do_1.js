//push to front
//Given an array and an additional value, insert this value at the beginning of the array. Do this without using any built-in array methods.

function pushTofront(arr,val){
    for(var i= arr.length-1;i>=0;i--){
        arr[i+1] = arr[i];
    }
    arr[0] =val;
}
var x = [2,3,5,8,9]
pushTofront(x,7)
console.log(x)

//Pop Front
//Given an array, remove and return the value at the beginning of the array. Do this without using any built-in array methods except pop().

function popFront(arr){
    var returnVal = arr[0];
    for (var i = 1; i < arr.length; i++) {
        arr[i-1] = arr[i];
    }
    arr.pop();
    return returnVal;
}
var x = [2,3,5,8,9,10]
popFront(x)
console.log(x)
let y = [13,114,27,30]
popFront(y)
console.log(y)


//Insert At
//Given an array, index, and additional value, insert the value into array at given index. Do this without using built-in array methods. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val).

function insertAt(arr, val, index) {
    for (var i= arr.length-1; i >= index; i--) {
        arr[i+1] = arr[i];
    }
    arr[index] = val;
}
let x1 = [9,5,1,4,7]
insertAt(x1,8,3)
console.log(x1)
let y1 = [7,8,5]
insertAt(y1,1,0)
console.log(y1)

//Remove At (Bonus Challenge)
//Given an array and an index into array, remove and return the array value at that index. Do this without using built-in array methods except pop(). Think of popFront(arr) as equivalent to removeAt(arr,0).

function removeAt(arr, ind) {
    ind = Math.floor(ind);
    if (ind >= arr.length || ind < 0) {
        return null; 
    }
    var returnVal = arr[ind];
    for (var i = ind + 1; i < arr.length; i++) {
        arr[i-1] = arr[i];
    }
    arr.pop();
    return returnVal;
}
let x2 =[0,9,2,4]
removeAt(x2,2)
console.log(x2)


//Swap Pairs (Bonus Challenge)
//Swap positions of successive pairs of values of given array. If length is odd, do not change the final element. For [1,2,3,4], return [2,1,4,3]. For example, change input ["Brendan",true,42] to [true,"Brendan",42]. As with all array challenges, do this without using any built-in array methods.

function swapPairs(arr) {
    for (var i = 0; i < arr.length - 1; i += 2) {
        var temp = arr[i];
        arr[i] = arr[i+1];
        arr[i+1] = temp;
    }
}
let x3 =[1,2,6,7,0,9]
swapPairs(x3)
console.log(x3)

//Remove Duplicates (Bonus Challenge)
//Sara is looking to hire an awesome web developer and has received applications from various sources. Her assistant alphabetized them but noticed some duplicates. Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. As with all these array challenges, do this without using any built-in array methods.

function removeDupesV1(arr) {
    for (var i = 0; i < arr.length - 1; i++) {
        if (arr[i+1] == arr[i]) {
            while (arr[i+1] == arr[i]) {
                removeAt(arr,i+1);
            }
        }
    }
}