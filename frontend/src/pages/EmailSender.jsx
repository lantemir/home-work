import React, { useState, useEffect } from 'react'
import s from './EmailSender.module.css';
import axios from 'axios';
import * as bases from '../components/bases'



function EmailSender() {

    const [email, setEmail] = useState('');
    const [subject, setSubject] = useState('');
    const [message, setMessage] = useState('');



    const sendEmail = (e) => {
        e.preventDefault();        

         let data = new FormData();
         data.append("email",  email);
         data.append("subject", subject);
         data.append("message", message);

         axios.post('/api/sendemail/', data)
            .then(res => console.log(res))
            .catch(errors => console.log(errors))
        

    }




    return (
        <div>
            <bases.Base1>
            <h1>Отправка писем</h1>

            <div className={s.formShow}>
                <form onSubmit={sendEmail}>
                    <input onChange={(e)=> setEmail(e.target.value)} type="text" value={email} placeholder='кому отправить email' name='emailreceiver' />
                    <input onChange={(e)=> setSubject(e.target.value)} type="text" value={subject}  placeholder='тема письма' name='subject' />
                    <textarea onChange={(e)=> setMessage(e.target.value)} type="text" value={message} placeholder='текст письма' name='messageinfo' rows="4" cols="50"></textarea>

                    <button>Отправить</button>

                </form>

            </div>

            </bases.Base1>
        </div>
    )
}

export default EmailSender