import React from 'react';
import TodoInput from './components/TodoInput'
import TodoList from './components/TodoList';

const App = () => {
  return <div style={{width: "200px",margin: "0 auto"}}>
      <TodoInput/>
      <TodoList/>

    </div>
}

export default App;