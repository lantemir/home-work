import React, { useState, useEffect } from 'react'
import * as bases from '../components/bases'
import axios from "axios";


const Chat = () => {

    const testChat = () => {
        console.log("testChat")
        axios.get('')

    }



    useEffect(() => {
    //     const roomName = 'firstroom';
    
    //    // const chatSocket = new WebSocket('ws://'+ window.location.host +'/ws/chat/'+roomName+'/');



    //    const ws = new WebSocket('ws://'+ window.location.host +'/ws/socket-server/'); 









    //     console.log(chatSocket)

    //     chatSocket.onmessage =  (e) => {
    //         const data = JSON.parse(e.data)
    //         console.log(data)         

    //     }

    },[])


    return (
        <bases.Base1>
            <div>
                <h1>Чат</h1>

                <button onClick={testChat}>testChat</button>

            </div>

        </bases.Base1>


    )
}

export default Chat