
const SET_ICECREAM = 'SET_ICECREAM';
const SET_CURRENT_PAGE_ICECREAM = 'SET_CURRENT_PAGE_ICECREAM';
const SET_TOTAL_ICECREAM_COUNT = 'SET_TOTAL_STORIES_COUNT';


let initialState = {
    icecreams: [],
    pageSize: 3,
    totalIcereamsCount: 0,
    currentPage: 1,
};

const icecreamReducer = (state = initialState, action) => {

    switch (action.type){
        case SET_ICECREAM:{
            return{...state, icecreams: action.icecreams}
        }
        case SET_CURRENT_PAGE_ICECREAM: 
            return{
                ...state, currentPage: action.currentPage
            }
        case SET_TOTAL_ICECREAM_COUNT:
            return{
                ...state, totalIcereamsCount: action.totalIcereamsCount
            }

        default:
            return state;        
    }

}

export const setIcecrems = (icecreams) => ({type: SET_ICECREAM, icecreams})
export const setCurrentPageAction = (currentPage) => ({type: SET_CURRENT_PAGE_ICECREAM, currentPage})
export const setTotalStoriesCount = (totalIcereamsCount) => ({type: SET_TOTAL_ICECREAM_COUNT, totalIcereamsCount})


export const requestIcecreams = (icecreams, dispatch, totalIcereamsCount, currentPage) => {  

  
    dispatch(setCurrentPageAction(currentPage))
    dispatch(setTotalStoriesCount(totalIcereamsCount))

    dispatch(setIcecrems(icecreams))
}

export default icecreamReducer