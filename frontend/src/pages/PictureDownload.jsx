import React, { useState, useEffect, useContext } from 'react'
import s from './Login.module.css';
import axios from 'axios';
import * as bases from '../components/bases'
import { useDispatch, useSelector } from 'react-redux';
import { requestToken } from '../app/redux/token-reducer';
import { useNavigate } from 'react-router-dom';




const PictureDownload = () => {

   

    const token = localStorage.getItem('tokenHomeWork')
     

    const [url, setUrl] = useState('');
   

    // let {loginUser} = useContext(AuthContext)


    const submit = async (e) => {
        e.preventDefault();

        const config = {
            headers:{Authorization: `Bearer ${token}`}
        };

        const bodyParameters = {
            "url": url
        }

        console.log('react url')
        console.log(url)

        axios.post("/api/download_img/", bodyParameters, config).then(
          response =>{            
            console.log(response)            
          }
        ).catch(
          error => {
            console.log(error.response)
           
          }
        )

        
     

        // await fetch('/api/login/', {
        //     method: 'POST',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify({
              
        //         email,
        //         password
        //     })
        // })


        // setRedirect(true);
    }

    const showtoken = () => {
        console.log(token)
    }

  return (
    <div>
        <bases.Base1>
        <h1>Скачиваем картинки, файлы</h1>

        <form onSubmit={ submit}>
            <input onChange={ (e) => setUrl(e.target.value)} value={url}  type="text"  placeholder='url для скачки'/>
          
            <button>Скачать</button>
        </form>

        <button onClick={showtoken}>показать токен</button>

       
        </bases.Base1>
    </div>
  )
}

export default PictureDownload