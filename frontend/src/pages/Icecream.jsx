import React, { useState, useEffect } from 'react'
import * as bases from '../components/bases'
import axios from 'axios';

const Icecream = () => {

  const [iceCreams, seticeCreams] =  useState([]);

  useEffect( () => {
   GetIceCreams(); 
  },[])

  async function GetIceCreams() {
        
    
    const config = {
      method: "GET",
      timeout: 5000,
      url: `/api/icecream/`
    }
    const response = await axios(config)
    
    console.log(response.data.list)
    seticeCreams(response.data.list)
    
  }


  const getIceCream = (e) => {
    e.preventDefault()
    console.log(iceCreams)
  }

  return (
    
    <bases.Base1>
    
    <div>
      <h1>Icecream</h1>


     

     
       {iceCreams.map(item => (
        
           <div key={item.id} className="card d-flex"  >
         
          <div className="card-body">
            <h5 className="card-title">{item.title}</h5>
            <p className="card-text">{item.description}</p>
            <ul>
              {item.comments.map(item => (
                <li key={item.id}>{item.comment_text}</li>
              ))}
            </ul>
            <h3>likes: {item.likes.likeCount}</h3>
          </div>
        </div>
       
        ))
       }

       

      </div>
      
      <button onClick={getIceCream}>getIceCream</button>
    </bases.Base1>
  )
}

export default Icecream