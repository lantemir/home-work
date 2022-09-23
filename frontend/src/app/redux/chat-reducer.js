
const SET_MESSAGES = 'SET_CHAT';
// const SET_CURRENT_PAGE_ICECREAM = 'SET_CURRENT_PAGE_ICECREAM';
// const SET_TOTAL_ICECREAM_COUNT = 'SET_TOTAL_STORIES_COUNT';


let initialState = {
    messages: [],
    
};

const chatReducer = (state = initialState, action) => {

    switch (action.type){
        case SET_MESSAGES:{
            return{...state, messages: action.messages}
        }
       

        default:
            return state;        
    }

}

export const setmessages = (messages) => ({type: SET_MESSAGES, messages})


export const requesmessages = (messages, dispatch) => {  
    dispatch(setmessages(messages))
}

export default chatReducer