/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    // Array.map is a method on array prototype
    //      - it accepts the array as 1st argument
    // callback provided to Array.map passes a reference to original array
    // as 3rd argument
    // 
    // the following approachs include approx benchmark results
    // test results for yourself on playground
    // test are done with a random array of 5*10^6 integers
    // and a callback that increments each number

    // in javascript, you can read and write to 

    const newArr = [];
    for (let i=0; i < arr.length; i++){
        newArr.push(fn(arr[i], i));
    }
    return newArr;
};
