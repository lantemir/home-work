import React, { useState } from "react";
import axios from 'axios';

const Jsonplaceholder = () => {

  const [message, setMessage] = useState("");

    async function getJsonplaceholder() {
        const config = {
            method: "GET",
            timeout: 5000,
            url: `https://jsonplaceholder.typicode.com/posts`, 

            
        }
        const response = await axios(config)

        console.log(response.data)
    }


    async function SendPost(e) {
      e.preventDefault();

     
      console.log(message);
      // const config = {
      //   method: "POST",
      //   timeout: 5000,
      //   url: `api/jsonplaceholder/`, 
      // }

       const formData = new FormData();
       formData.append("sendMessage", message)

       const response = await axios.post(`/api/jsonplaceholder/`, formData);

       console.log(response);
    }


  return (
    <div>
        <h1>Jsonplaceholder</h1>

        <button onClick={getJsonplaceholder}>get</button>

        <form onSubmit={SendPost} >
          <input type="text"  value={message} onChange={(e)=>setMessage(e.target.value)}/>
          <button>Post</button>
        </form>


    </div>
  )
}

export default Jsonplaceholder