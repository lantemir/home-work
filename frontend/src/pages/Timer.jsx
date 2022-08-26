import React, {useState, useEffect} from 'react'
import * as bases from '../components/bases'

const Timer = () => {
    const [seconds, setSeconds] = useState(60)
    const [timerActive, setTimerActive] = useState(false);


useEffect(()=>{
    if (seconds > 0 && timerActive) {
        setTimeout(setSeconds, 1000, seconds - 1);
      } else {
        setTimerActive(false);
      }
    }, [ seconds, timerActive ]);
  



  return (

    <bases.Base1>
        <div>Timer</div>

        {seconds
            ? <div> <button onClick={()=> setTimerActive(!timerActive)}> 
                {timerActive ? 'stop' : 'start'}
            </button>
            <div>{seconds}</div>
            </div>
            : <button onClick={() => setSeconds(60)}>ещё раз</button>

        }
    </bases.Base1>
    
  )
}

export default Timer