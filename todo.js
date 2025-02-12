document.addEventListener('DOMContentLoaded', function () {
  const todoList = document.getElementById('todo-list');

  axios.get('https://dummyjson.com/todos')
    .then(function (response) {
      const todos = response.data.todos;

      todos.map(function (todo) {
        const item = document.createElement('li');
        item.textContent = "id:"+todo.id+" todo:"+todo.todo;
        todoList.appendChild(item);
      });
    })
  });