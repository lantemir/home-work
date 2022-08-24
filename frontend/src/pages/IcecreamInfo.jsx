import React, { useState, useEffect } from 'react'
import * as bases from '../components/bases'
import axios from 'axios';
import s from './IcecreamInfo.module.css';
import Paginator from '../components/Paginator/Paginator';
import { requestIcecreamsComments } from '../app/redux/comment-icecream-reducer';
import {useParams} from "react-router-dom"

import { useDispatch, useSelector } from "react-redux";


const IcecreamInfo = () => {
    const {id} = (useParams())
    const dispatch = useDispatch();

    const commentStore = useSelector(state => state.CommentIcecreamR);
      const {
        iceCreamInfo,
        comments,
        pageSize: pageSize,
        totalCommentCount,
        currentPage,
      } = commentStore



    useEffect(() => {
        
        GetIcecreamInfo(id, currentPage, dispatch);
        
    },[])

    async function GetIcecreamInfo(id, currentPage, dispatch) {
        const config = {
            method: "GET",
            timeout: 5000,
            url: `/api/icecream/${id}`, 

            params: {
                currentPage: currentPage,
                pageSize: pageSize
            },
        }
        const response = await axios(config)

        console.log(response.data)
        // seticeCreams(response.data.list)

       requestIcecreamsComments(response.data.icecream_obj, dispatch, response.data.x_total_count_comment, currentPage, response.data.comment )

    }

    const testreduxstate = () => {
        console.log("commentStore")
        console.log(commentStore)
    }

    const onPageChanged = (pageNumber) => {
        console.log("onPageChanged")
        GetIcecreamInfo(id, pageNumber, dispatch )
    }


    return (

        <bases.Base1>
        <div className={`${s.wrapper} ${s.redBorder}`}>
            <h1 className={s.h1}>IcecreamInfo</h1>
            <div >
                <h2>{iceCreamInfo.title}</h2>
                <p>{iceCreamInfo.description}</p>
                <div>
                    <ul>
                        {comments.map(item => {
                            return(
                                <li key={item.id}>{item.comment_text}</li>
                            )
                        })}
                      
                    </ul>
                </div>
            </div>
            <div className={`${s.paginator}`}>
                Paginator
                <Paginator currentPage={currentPage} totalIcereamsCount={totalCommentCount} pageSize={pageSize} onPageChanged={onPageChanged}/>         
            </div>  
           
            
        </div>
        
        </bases.Base1>
    )
}

export default IcecreamInfo