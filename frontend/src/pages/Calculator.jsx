import React, {useState, useEffect} from 'react'
import * as bases from '../components/bases'
import s from './Calculator.module.css';

const Calculator = () => {

    const [result, setResult] = useState('');

    const handleClick = (e) => {
        setResult(result.concat(e.target.name));
    }
    const clear = () => {
        setResult('');
    }
    const backspace = () => {
        setResult(result.slice(0, result.length - 1 ));
    }
    const calculate = () => {
        try{
            setResult(eval(result).toString());
        }catch(err){
            setResult("Error")
        }        
    }

  return (

    <bases.Base1>
    <div className={s.calculator}>
        <div className={s.container}>
            <form>
                <input type="text" value={result}/>
            </form>
            <div className={s.keypad}>
                <button className={s.highlight} onClick={clear} id={s.clear}>Clear</button>
                <button className={s.highlight} onClick={backspace} id={s.backspace}>C</button>
                <button className={s.highlight} name="/" onClick={handleClick}>&divide;</button>
                <button name="7" onClick={handleClick}>7</button>
                <button name="8" onClick={handleClick}>8</button>
                <button name="9" onClick={handleClick}>9</button>
                <button className={s.highlight} name="*" onClick={handleClick}>&times;</button>
                <button name="4" onClick={handleClick}>4</button>
                <button name="5" onClick={handleClick}>5</button>
                <button name="6" onClick={handleClick}>6</button>
                <button className={s.highlight} name="-" onClick={handleClick}>&ndash;</button>
                <button name="1" onClick={handleClick}>1</button>
                <button name="2" onClick={handleClick}>2</button>
                <button name="3" onClick={handleClick}>3</button>
                <button className={s.highlight} name="+" onClick={handleClick}>+</button>
                <button name="0" onClick={handleClick}>0</button>
                <button name="." onClick={handleClick}>.</button>
                <button className={s.highlight} onClick={calculate} id={s.result}>=</button>                
            </div>
        </div>        
    </div>
    </bases.Base1>    
  )
}

export default Calculator