// import React, { useState, useEffect } from 'react'
// import * as bases from '../components/bases'
// import axios from 'axios';
// import s from './Icecream.module.css';
// import Paginator from '../components/Paginator/Paginator';
// import { requestIcecreamsComments } from '../app/redux/comment-icecream-reducer';

// import { useDispatch, useSelector } from "react-redux";





//  const IcecreamComment = (props) => {

  

//   useEffect( () => {
//     console.log("GetCommentsIceCreams");
//     GetCommentsIceCreams(currentPage); 
//    },[])

//   const dispatch = useDispatch();

  

//   const commentStore = useSelector(state => state.CommentIcecreamR);
//   const {
//     comments,
//     pageSize: pageSize,
//     totalIcereamsCount,
//     currentPage,
//   } = commentStore

//   async function GetCommentsIceCreams(currentPage) {
        
    
//         const config = {
//           method: "GET",
//           timeout: 5000,
//           url: `/api/commenticecream/${props.icecream_id}`,
    
//           params: {
//               currentPage: currentPage,
//               pageSize: pageSize
//           },
//         }
//         const response = await axios(config)
    
    
        
//         // console.log(response.data.x_total_count)
//         // seticeCreams(response.data.list)
    
//         requestIcecreamsComments(response.data.list, dispatch, response.data.x_total_count, currentPage)
        
//   }

    
//   const onPageChanged = (pageNumber) => {
//     GetCommentsIceCreams(pageNumber)    
//   }

//   const CheckRedux = (e) => {
//     e.preventDefault();
//     console.log(comments)
//   }

//   return (
//     <div>
//         <ul>
//             {comments.map(item => (
//                 <li key={item.id}>{item.comment_text}</li>
//             ))}
//         </ul> 

//         {/* <Paginator currentPage={} totalIcereamsCount={} pageSize={} onPageChanged={}/> */}
//         <button onClick={CheckRedux}>CheckRedux</button>
//     </div>   
//   )
// }

// export default IcecreamComment
















// // Вариант передачи через props
// // import React from 'react'

// //  const IcecreamComment = (props) => {
// //   return (
// //     <div>
// //         <ul>
// //             {props.comments.map(item => (
// //                 <li key={item.id}>{item.comment_text}</li>
// //             ))}
// //         </ul> 

// //         <Paginator currentPage={} totalIcereamsCount={} pageSize={} onPageChanged={}/>
// //     </div>   
// //   )
// // }

// // export default IcecreamComment