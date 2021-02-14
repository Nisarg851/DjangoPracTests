//Element
const listOfItem = document.querySelector(".list");

//Event Handler
listOfItem.addEventListener("click",checkOrDeleteTODO);

//Funtion to check or delete item from the list
function checkOrDeleteTODO(e){
    const todo = e.target;
    if(todo.classList[1]=='btn-trashbtn'){
        const todoParent = todo.parentElement;
        todoParent.classList.toggle('todo-delete');
        // removeTodoFromLocalStorage(todoParent);
        // todoParent.addEventListener('transitionend',function(){
        //     todoParent.remove();
        // });
    }
    if(todo.classList[1]=='btn-checkbtn'){
        const todoParent = todo.parentElement;
        todoParent.classList.toggle('todo-done');
    }
}

