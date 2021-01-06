// 1. javascript는 일급함수
// 함수 정의, 함수 호출에서 사용
// 정의 : function([parameter, parameter, ...]) { 구현; [return data;]}
// 호출 : 함수명([parameter값, parameter값, ...])
// parameter, return data에 함수 사용 가능
// ====
// let functionV = function([parameter, parameter, ...]) { 구현;  [return ]}

// 클로저
// 함수에서 다른 함수 리턴
function makeAdder(x) {
    let y = 1; // makeAdder function local variable
    
    // z function
    return function(z) { // 외부에서 로컬 변수인 y에 접근하려면 이 함수로 접근하면 된다.
        y = 100; // 외부 함수 local variable 사용
        return x + y + z;
    }
}

let add5 = makeAdder(5); // z function이 add5가 된다.
let add10 = makeAdder(10); // z function이 add10이 된다.
console.log(add5(2), add5);
console.log(add10(2), add10);

// 클로져
function multi(n) {
    return function() {
        return n * n;
    }
}

let multi5 = multi(5);
let multi10 = multi(10);
console.log(multi5, multi5());
console.log(multi10, multi10());

// 재귀함수
let result = 1;

function factorial(n) {
    if (n == 0) {
        console.log(`호출 끝`);
    }
    else {
        console.log(`호출 ${n}`);
        result *= n;
        factorial(n - 1);
    }

    return result;
}

console.log(`10! = ${factorial(10)}`);