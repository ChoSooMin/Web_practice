// 1. var, const
var x; // 변수 선언
x = 6; // 값 할당

// 2. const
const constVariable = 10; // const는 값이 변경되지 않는 상수값이다. (read only)

// 3. let
let globalVariable = 5;
{
    let localVariable = 5;
    var y = 5; // var은 local에서 선언해도 global에서 사용이 가능하다.

    console.log(`========== local ==========`);
    console.log(`globalVariable = ${globalVariable}`);
    console.log(`localVariable = ${localVariable}`);
    console.log(`var x = ${x}`);
    console.log(`var y = ${y}`);
    console.log(`constVariable = ${constVariable}`);
}
console.log(`========== global ==========`);
console.log(`globalVariable = ${globalVariable}`);
// console.log(`localVariable = ${localVariable}`); // Error! 로컬 변수를 글로벌에서 쓰려함
console.log(`var x = ${x}`);
console.log(`var y = ${y}`);

// 2. constVariable 변경해보기
// constVariable = 4; // Error! 상수에 값 할당
console.log(`constVariable = ${constVariable}`);

document.getElementById("data").innerHTML = `<h3>variable x = ${x}</h3>`;