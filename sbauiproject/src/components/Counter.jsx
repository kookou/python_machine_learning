import React, { useState } from 'react'
const Counter = () => {
    let [count, setCount] = useState(0)
    const handleClick =() => {
        setCount(count + 1)
    }
    const handleClick2 =() => {
        setCount(count - 1)
    }
    return <>
        <h1>counter : {count} </h1>
        <button onClick={handleClick}> + </button>  
        <button onClick={handleClick2}> - </button>    
    </>
}
export default Counter