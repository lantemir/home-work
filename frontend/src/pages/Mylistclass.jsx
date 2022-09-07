import React, {useState, useEffect} from 'react'
import * as bases from '../components/bases'
import s from './Mylistclass.module.css';
import axios from 'axios';


function Mylistclass() {

    const [dataInfo, setDataInfo] = useState([]);
    const [users, setUsers] = useState([]);

    const [selectedUserId, setSelectedUserId] = useState('0');


    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [objIdForUpdate, setobjIdForUpdate] = useState('0');

    useEffect(()=>{
          axios.get(`/api/mylistdj`)
            .then(res => {
                const data = res.data;
                console.log(data)       
                setDataInfo(data.data);
                setUsers(data.users)         
            })
    },[])

    

    const GetClassData = async (e) => {
        e.preventDefault()

        console.log(selectedUserId)
        console.log(typeof(selectedUserId))

        // const config = {
        //     method: "GET",
        //     timeout: 5000,
        //     url: `/api/mylistdj/`, 

          

            
        // }
        // const response = await axios(config)

        // console.log(response)
        // setDataInfo(response)

        // axios.get(`/api/mylistdj`)
        //     .then(res => {
        //         const data = res.data;
        //         console.log(data)
        //         setDataInfo(data)
        //     })
    }

    const selectedUser = (e) => {
        e.preventDefault();
        setSelectedUserId(e.target.value)
        // setSelectedUserName(e.target.value)
        // console.log(e.target.value)
        console.log(e.target.value)
    }

    const sendPostReq = (e) => {
        e.preventDefault();

        axios.post(`/api/mylistdj/`, {selectedUserId, title, description })
            .then(res => {
                const data = res.data;                
                setDataInfo(data.data);             
            })
        setSelectedUserId('0');    
        setTitle('');
        setDescription('');
        
    }

    const deleteTask = (e, item_id) => {
        e.preventDefault();   

        axios.delete(`/api/mylistdj/${item_id}`)
        .then(res => {
            const data = res.data;               
            setDataInfo(data.data);             
        })
    }

    const updateTask = (e, item_id) => {
        e.preventDefault();

        let needObj =  dataInfo.filter(item => item.id == item_id)

        setTitle(needObj[0].title)
        setDescription(needObj[0].description)
        setSelectedUserId(needObj[0].users[0].id) 
        setobjIdForUpdate(needObj[0].id)

       
    }


    const updateResponse = (e) => {
        e.preventDefault();

        axios.put(`/api/mylistdj/`, {selectedUserId, title, description, objIdForUpdate })
        .then(res => {
            const data = res.data;    
            console.log(data)            
            setDataInfo(data.data)          
        })


        setSelectedUserId('0');      
        setTitle('');
        setDescription('');

    }


    return (
        <div>
            <bases.Base1>

                <h1>Mylistclass</h1>

                <div>
                    <form  className={s.formBlock} onSubmit={sendPostReq}>
                        <input onChange={(e) => setTitle(e.target.value) } value={title} type="text" placeholder='Заголовок' />
                        <textarea onChange={(e) => setDescription(e.target.value)} value={description} type="text" placeholder='описание' />
                        
                        <select  value={selectedUserId} onChange={selectedUser}>
                                 <option key={0} value={0}>Выберите пользователя</option>
                            {
                                users && users.map(item => (
                                    <option key={item.id}  value={item.id} > {item.username}</option>
                                )) 
                            }
                        
                        </select>
                        <button>Отправить</button>
                        
                    </form>

                    <button onClick={updateResponse}>Обновить</button>
                </div>

                <div>
                    <ul>
                        {dataInfo && dataInfo.map(item => (
                            <li key={item.id} className={s.listyle}>{item.title}  -{item.description}  - <button onClick={ (e) => deleteTask(e,item.id)}>Удалить</button> - <button onClick={ (e) => updateTask(e,item.id)}>Обновить</button></li>
                            
                        ))
                        
                        }
                    </ul>
                </div>


                <button onClick={GetClassData}>GetClassData</button>

            </bases.Base1>

        </div>

    )
}

export default Mylistclass