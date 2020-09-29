import React from 'react'
import {useSelector, useDispatch} from 'react-redux'

const TodoList = () => {
    const todos = useSelector(state => state.todos) // 함수처리 state.todos을 리턴한다 
    const dispatch = useDispatch()
    const toggleTodo = todoId => dispatch(toggleTodoAction(todoId))
    const deleteTodo = todoId => dispatch(deleteTodoAction(todoId))

    return <>
    {
        todos && todos.length === 0 && (
            <p>No Todo at the moment</p>
        )
    }
    {todos && 
        todos.map(todo => (
            <div key={todo.id}>
                <div>
                    <input type="checkbox" checked={todo.complete}
                    onChange = {toggleTodo.bind(null, todo.todoId)}
                    />
                    <span style={{margin: '20px'}}>{todo.name}</span>
                    <button onClick={deleteTodo.bind(null,todo.todoId)}>
                        X
                    </button>
                </div>
            </div>
        ))}
    
    </>  // new jss
}
export default TodoList