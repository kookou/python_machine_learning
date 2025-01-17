import React, {useState} from 'react'
import uuid from 'uuid/v4'
import {useDispatch} from 'react-redux'
import {addTodoAction} from '../store/todoReducer'

const TodoInput = () => {
    //todo 가 CRUD 대상(object) 이다. -> 속성이된다.
    //es6 이전모드는 var
    //es6 이후 let, const 두가지로 정의 변수, 상수 (문자열도 해당)
    //함수는 const 타입에 할당한다.
    //기능과 속성이 함께 묶여 있을 경우 객체가 된다.  = const
    //JSON = Javascript Object Notation
    //object {'':'','':()=>{} } , array []
    //객체 = 기능 + 속성
    //함수 = 기능
    //함수 = 객체 - 속성
    //변수 = 객체 - 함수


    const [todo, setTodo] = useState('') // Redux 를 사용하는 중 
    const dispatch = useDispatch()
    const submitForm = e => {
        e.preventDefault() // default 기능은 막고, 내가 정의한 기능을 구현해라.
        const newTodo = {
            todoId: uuid(),
            name: todo,
            complage : false
        }
        addTodo(newTodo)
        setTodo("")
        document.getElementById('input').value = ""
    }

    const handleChange = e => {
        e.preventDefault()
        setTodo(e.target.value)
    }

    const addTodo = todo =>{
        dispatch(addTodoAction(todo)) // 영속적으로 저장할 곳 state -> api -> database
    }

    return <>
    <h1>할리 갈리</h1>
    <form onSubmit={submitForm} method='POST'>
        <div>
            <input type="text" name="todo" id="input" onChange={handleChange}/><br/>
            <input type="submit" value="SUBMIT"/>
        </div>
    </form>
    </>
}

export default TodoInput