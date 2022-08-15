import React, { useState, useEffect } from 'react'
import * as bases from '../components/bases'
import './Weather.css';
import axios from 'axios';

export function Weather() {

    const [city, setCity] =  useState([]);
    const [chosenCityId, setChosenCityId] = useState();

    const [cityShow, setCityShow] = useState('');
    const [sign, setSign] = useState('');
    const [temperature, setTemperature] = useState('');

    useEffect( ()=>{
      GetWeathe();
    },[])

    async function GetWeathe() {
        
    
        const config = {
          method: "GET",
          timeout: 5000,
          url: `/api/weather/`
        }
        const response = await axios(config)
        
        console.log(response.data.list)
        setCity(response.data.list)
        
      }

       const choseCity = async (e) => {
          e.preventDefault()
          // console.log(chosenCityId)

        const config = {
          method: "GET",
          timeout: 5000,
          url: `/api/weather/${chosenCityId}`
        }
        const response = await axios(config)
        
        console.log(response)

        setSign(response.data.sign)
        setTemperature(response.data.temp)
        setCityShow(response.data.city)


      } 

      const handleChange = (e) =>{
        e.preventDefault()
        setChosenCityId(e.target.value)
        
      }


  return (
    <bases.Base1>
      <div>Weather</div>
      <form onSubmit={choseCity}>
        <label>
          Выберите город:
          <select onChange={handleChange}>
            { city.map(item => (
                 <option key={item.id} value={item.id}>{item.city_name}</option>
            ))
            
            }
           
          </select>
        </label>
        <input type="submit" value="Отправить" />
      </form>
      <div>
      <div className="card">
        {/* <img src="" className="card-img-top" alt="..."/> */}
          <div className="card-body">
            <h5 className="card-title">{cityShow}</h5>
            {temperature&& <p className="card-text">Температура: {sign}{temperature} градусов.</p>}
        
          </div>
      </div>
      </div>
      {/* <button onClick={GetWeathe} className='btn btn-lg btn-outline-danger'>GetWeathe</button> */}
      
    </bases.Base1>
  )
}

