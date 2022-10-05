import React, { useState, useEffect } from 'react'
import s from './Register.module.css';
import axios from 'axios';
import * as bases from '../components/bases'
import { Navigate } from 'react-router-dom';


function Register() {

    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [redirect, setRedirect] = useState(false);


    const submit = async (e) => {
        e.preventDefault();

        //  let data = new FormData();
        //  data.append("email",  email);
        //  data.append("subject", subject);
        //  data.append("message", message);

        //  axios.post('/api/sendemail/', data)
        //     .then(res => console.log(res))
        //     .catch(errors => console.log(errors))

        await fetch('/api/register/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                name,
                email,
                password
            })
        })

        // const content = await response.json();
        // console.log(content);
        setRedirect(true);
    }

    if (redirect) {
        return <Navigate to="/login" />
    }

    return (
        <div>
            <bases.Base1>
                <h1>Регистрация</h1>

                <form onSubmit={submit}>
                    <input onChange={(e) => setName(e.target.value)} value={name} type="text" placeholder='Name' />
                    <input onChange={(e) => setEmail(e.target.value)} value={email} type="text" placeholder='email ' />
                    <input onChange={(e) => setPassword(e.target.value)} value={password} type="password" placeholder='password' />
                    <button>регистрация</button>
                </form>
            </bases.Base1>
        </div>
    )
}

export default Register