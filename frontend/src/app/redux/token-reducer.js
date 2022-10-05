
const LOAD = "LOAD";
const SUCCESS = "SUCCESS";
const ERROR = "ERROR";
const DELETETOKEN = "DELETETOKEN";

let initialState = {
    load: false,
    token: null,
    error: false,
};


// Reducer - "Переключатель состояния хранилища"
const TokenReducer = (state = initialState, action  ) =>{
    
    switch(action.type){ // switch ("LOAD") 
        case LOAD:{
            return {"load": true}
        }
        case SUCCESS: {
            return{ ...state,  load: false, token: action.token};
        }
        case DELETETOKEN: {
            return{ ...state,  load: false, token: null};
        }
        


        case ERROR: {
            return{load: false, token: undefined, error: "произошла ошибка" }
        }
        default: return state;

    }
}



export const setToken = (token) => ({type: SUCCESS, token})
export const deleteToken = () => ({type: DELETETOKEN})

export const requestToken = (token, dispatch) => {  
    dispatch(setToken(token))
    localStorage.setItem('tokenHomeWork', token )
}

export const requestDeleteToken = (dispatch) => {
    dispatch(deleteToken)
    localStorage.removeItem('tokenHomeWork')
}


export default TokenReducer;