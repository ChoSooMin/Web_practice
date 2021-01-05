// 1. 산술연산자(+, -, *, /, %)
let z = 20;
let w = 10;

console.log(`z = ${z}`);
console.log(`w = ${w}`);
console.log(`z + w = ${z + w}`);
console.log(`z - w = ${z - w}`);
console.log(`z * w = ${z * w}`);
console.log(`z / w = ${z / w}`);
console.log(`z % w = ${z % w}`);

// 2. 대입 연산자 =
w = 2;
console.log(`w = ${w}`);

// 3. 비교 연산자 >, <, >=, <=, ==, !=
if (z < w) {
    console.log(`z bigger than w`);
}
else {
    console.log(`w bigger than z`);
}

// 4. 논리 연산자 &&, ||, ^, ~
if (z != w) {
    console.log(`z not equal w`);
}
else {
    console.log(`z equal w`);
}

// 5. 비트 연산자 &, |, ~
console.log(`z | w = ${z | w}`);

// 6. 삼항 연산자 [조건 ? 참 : 거짓]
(z <= w) ? console.log(`z lower than w`) : console.log(`w lower than z`);