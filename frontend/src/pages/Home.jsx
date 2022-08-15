import axios from 'axios'
import React from 'react'
import { useDispatch, useSelector } from 'react-redux';
import * as bases from '../components/bases'

export const GET_ALL_MESSAGE_LOAD = "GET_ALL_MESSAGE_LOAD";
export const GET_ALL_MESSAGE_DATA = "GET_ALL_MESSAGE_DATA";
export const GET_ALL_MESSAGE_ERROR = "GET_ALL_MESSAGE_ERROR";
export const GET_ALL_MESSAGE_FAIL = "GET_ALL_MESSAGE_FAIL";
export const GET_ALL_MESSAGE_RESET = "GET_ALL_MESSAGE_RESET";

export function GetAllMessageReducer(state={}, action=null ){
  switch (action.type){
    case GET_ALL_MESSAGE_LOAD:
      return {load: true}
    case GET_ALL_MESSAGE_DATA:
      return {load: false, data: action.payload}
    case GET_ALL_MESSAGE_ERROR:
        return {error: 'Ошибка на сервере'}
    case GET_ALL_MESSAGE_FAIL:
      return {fail: 'Ошибка на клиенте'}
    case GET_ALL_MESSAGE_RESET: 
        return {}
    default:
      return state
  }
}

export function Home() {
  const dispatch = useDispatch();

  const textInfo = useSelector((state) => state.GetAllMessage.data)


  async function GetAllSms() {
    dispatch({type: GET_ALL_MESSAGE_LOAD})

    const config = {
      method: "GET",
      timeout: 5000,
      url: `/api/chat/?page=1&limit=3`
    }
    const response = await axios(config)
    
    console.log(response.data.list)
    dispatch({type: GET_ALL_MESSAGE_DATA, payload: response.data.list}) 
  }


  const showuseSelector = () => {
    console.log(textInfo)
  }


  return (

    <bases.Base1>
      <div> <h1>Home2</h1>
        <button onClick={GetAllSms} className = 'btn btn-lg btn-outline-danger'>GetAllSms</button>
        asd
        <button onClick={showuseSelector}>useSelector</button>
      </div>
    </bases.Base1>

  )
}

