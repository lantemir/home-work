import React, { useState, useEffect } from 'react'
import * as bases from '../components/bases'
import axios from 'axios';
import s from './Icecream.module.css';
import Paginator from '../components/Paginator/Paginator';
import { requestIcecreams } from '../app/redux/icecream-reducer';

import { useDispatch, useSelector } from "react-redux";


const Icecream = () => {

  // const [iceCreams, seticeCreams] =  useState([]);

  useEffect( () => {
   GetIceCreams(currentPage); 
  },[])


  const dispatch = useDispatch();

  const iceCreamStore = useSelector(state => state.IcecreamR);
  const {
    icecreams,
    pageSize: pageSize,
    totalIcereamsCount,
    currentPage,
  } = iceCreamStore

  async function GetIceCreams(currentPage) {
        
    
    const config = {
      method: "GET",
      timeout: 5000,
      url: `/api/icecream/`,

      params: {
          currentPage: currentPage,
          pageSize: pageSize
      },
    }
    const response = await axios(config)


    
    // console.log(response.data.x_total_count)
    // seticeCreams(response.data.list)

     requestIcecreams(response.data.list, dispatch, response.data.x_total_count, currentPage)
    
  }


  const getIceCreamLocalState = (e) => {
    e.preventDefault()
    console.log(icecreams)
  }

  const getIceCreamRedux = (e) => {
    e.preventDefault()
    console.log(iceCreamStore)
  }

  const onPageChanged = (pageNumber) => {
    GetIceCreams(pageNumber)    
  }

  return (

    <bases.Base1>

      <div className={`${s.wrapper}  ${s.redBorder}`}>

        <h1 className={s.h1}>Icecream</h1>
        <div className={s.flexContainer}>
        {icecreams.map(item => (

          <div key={item.id} className={s.blockInner}  >

            <div className="card-body">
              <h5 className={s.test}>{item.title}</h5>
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


        <Paginator currentPage={currentPage} totalIcereamsCount={totalIcereamsCount} pageSize={pageSize} onPageChanged={onPageChanged}/>
      </div>

      <button onClick={getIceCreamLocalState}>getIceCreamLocalState</button>

      <button onClick={getIceCreamRedux}>getIceCreamRedux</button>
    </bases.Base1>
  )
}

export default Icecream