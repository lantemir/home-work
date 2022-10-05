import React, { useState, useEffect, useContext } from 'react'
import s from './Login.module.css';
import axios from 'axios';
import * as bases from '../components/bases'
import { useDispatch, useSelector } from 'react-redux';
import { requestToken } from '../app/redux/token-reducer';
import { useNavigate } from 'react-router-dom';

// import AuthContext from '../context/AuthContext';





const Login = () => {

    const navigate = useNavigate();

    const dispatch = useDispatch();

    const token = useSelector(state => state.TokenR.token);
     

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const [showError, setShowError] = useState('');
    const [showErrorStatus, setShowErrorStatus] = useState('');

    // let {loginUser} = useContext(AuthContext)


    const submit = async (e) => {
        e.preventDefault();

        axios.post("/api/token/", {"username": email, "password": password }).then(
          response =>{
            
            requestToken(response.data.access, dispatch)
            // console.log(response)
            // console.log(response.data)
            // console.log(response.status)

            navigate('/');
          }
        ).catch(
          error => {
            console.log(error.response.data.detail)
            console.log(error.response.status)
            setShowError(error.response.data.detail)
            setShowErrorStatus(error.response.status)
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
        <h1>Login</h1>

        <form onSubmit={ submit}>
            <input onChange={ (e) => setEmail(e.target.value)} value={email}  type="text"  placeholder='email or login'/>
            <input onChange={ (e) => setPassword(e.target.value)} value={password}  type="password"  placeholder='password' />
            <button>Войти</button>
        </form>

        <button onClick={showtoken}>показать токен</button>

        {
          showErrorStatus == 401 ?
              showError : null
        }
        </bases.Base1>
    </div>
  )
}

export default Login