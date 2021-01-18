let todoInputHandler = function () {
    // todoList 객체에 데이터를 추가해야한다.
    // todoNum은 todoList.length() + 1로, todoStr은 들어온 값 그대로
    
    /**
    // todoNum 구하는 방법1 (Math 사용)
    const result = todoList.map(todo => todo.todoNum);
    const maxTodoNum = Math.max(...result); // Math.max.apply(null, )
    const addTitle = document.getElementById("todoInput").value;
    */
    
    // todoNum 구하는 방법2
    let todoLength = todoList.length;
    let todoString = document.getElementById("todoInput");
    let todoData = {
        todoNum: todoLength + 1,
        todoStr: todoString.value
    }; 

    todoList.push(todoData);
    
    // todoList 렌더링
    displayList()
};

let todoDeleteHandler = function (todoNum) {
    // todoList에서 todoNum에 해당하는 데이터 삭제
    const index = todoList.findIndex(todo => (todo.todoNum == todoNum));
    // const index = todoList.findIndex(todoNum); // todoNum에 해당하는 인덱스를 찾는다.
    todoList.splice(index, 1); // 배열에서 데이터 삭제하는 법, splice는 재할당 필요 없다.
    
    // todoList 렌더링
    displayList()
};

let todoClear = function () {
    // todoList 배열 empty
    // todoList 렌더링
    todoList = []; // empty

    // todoList 렌더링
    displayList()
};

function displayList() {
    const todos = document.getElementById("todos");
    var initTodoList = ``;

    todoList.forEach(todo => {
        // innerHTML보다는 DOM API를 사용하는 게 더 낫다. (appendAdd)
        initTodoList += `
                        <li class="shadow" style="user-select: auto;">
                            <i aria-hidden="true" class="checkBtn fa fa-check"></i>
                            ${todo.todoStr}
                            <span type="button" class="removeBtn" onclick="todoDeleteHandler(${todo.todoNum})">
                                <i aria-hidden="true" class="fa fa-trash-o"></i>
                            </span>
                        </li>
                        `;
    });

    todos.innerHTML = initTodoList;
}