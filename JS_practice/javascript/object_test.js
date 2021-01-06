// class : object를 생성하기 위한 template (요구사항을 추상화해서 속성과 ..)
// object : class type으로 생성된 변수 (클래스 new 생성자를 통해 인스턴스화된 객체)
// new : 메모리 공간 확보, 생성자 : 초기화

// 1. class 선언 (ECMA6 - class 키워드 제공_이전 버전에서는 제공이 안됨_function으로 사용했었다.)
/**
 * class 클래스 이름 {
 *      변수;
 *      메소드;
 * }
 */
class Person {
    // TypeScript에서는 타입을 앞에 넣어주는데 JS에서는 보통 변수 이름과 초기값만 설정해준다.
    /**
    name = "";
    age = 0;
     */
    _name = "";
    _age = 0;

    constructor(name, age) {
        // this는 JS에서 주의해서 사용해야 함
        // 때에 따라서는 this가 윈도우 창, 객체로 사용될 수도 있음
        // -> 이걸 대비해서 _name, _age로 사용하기도 함
        /**
        this.name = name;
        this.age = age;
         */
        this._name = name;
        this._age = age;
    }

    print() {
        console.log(`이름: ${this._name}, 나이: ${this._age}`);
    }
    
    // setter getter는 메소드 개념이 아니라 멤버 변수들이 어떤 로직에 의해 계산되어야 할 때 get 키워드를 가지고 계산을 해서 return 해준다.
    // 멤버 변수를 계산해서 return 해주는 경우에 사용
    get birthYear() {
        return 2021-this._age + 1;
    }

    // 변수에 action을 줘서 하고싶을 때.. 사용
    set birthYear(year) {
        this._age = 2021 - year + 1;
    }
}

let p = new Person("조수민", 25);
p.print();

// 2. function 객체로 선언
function Student(name, age, major) {
    this._name = name;
    this._age = age;
    this._major = major;
    this.print = function() { // 익명 함수 사용
        console.log(`이름: ${this._name}, 나이: ${this._age}, 전공: ${this._major}`);
    }
}

let s = new Student("조수민", 25, "컴퓨터학과");
s.print();

// 3. JSON(JavaScript Object Notation)
let e = { name: "조수민", age: 25, job: "backend programmer" };
console.log(e);
console.log(`이름: ${e.name}, 나이: ${e.age}, 직업: ${e.job}`);

let e1 = { person : { name: "조수민", age: 25, department: "연구소"}, birth: "1996-11-02", array: [1, 2, 3, 4] };
let array = [{ name: "조수민", age: 25 }, 1, [1, 2, 3, 4], 'name', "false", "null"];
console.log(e1);