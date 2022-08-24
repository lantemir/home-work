
const SET_COMMENT_ICECREAM = 'SET_COMMENT_ICECREAM';
const SET_CURRENT_PAGE_ICECREAM_COMMENT = 'SET_CURRENT_PAGE_ICECREAM_COMMENT';
const SET_TOTAL_ICECREAM_COMMENT_COUNT = 'SET_TOTAL_ICECREAM_COMMENT_COUNT';
const SET_ICECREAM_INFO = 'SET_ICECREAM_INFO';



let initialState = {
    iceCreamInfo: {},
    comments: [],
    pageSize: 3,
    totalCommentCount: 0,
    currentPage: 1,
};

const commentIcecreamReducer = (state = initialState, action) => {

    switch (action.type){
        case SET_COMMENT_ICECREAM:{
            return{...state, comments: action.comments}
        }
        case SET_CURRENT_PAGE_ICECREAM_COMMENT: 
            return{
                ...state, currentPage: action.currentPage
            }
        case SET_TOTAL_ICECREAM_COMMENT_COUNT:
            return{
                ...state, totalCommentCount: action.totalCommentCount
            }
        case SET_ICECREAM_INFO:
            return{
                ...state, iceCreamInfo: action.iceCreamInfo
            }

        default:
            return state;        
    }

}

export const setIcecremsComment = (comments) => ({type: SET_COMMENT_ICECREAM, comments})
export const setCurrentPageAction = (currentPage) => ({type: SET_CURRENT_PAGE_ICECREAM_COMMENT, currentPage})
export const setTotalStoriesCount = (totalCommentCount) => ({type: SET_TOTAL_ICECREAM_COMMENT_COUNT, totalCommentCount})

export const setIceCreamInfo = (iceCreamInfo) => ({type: SET_ICECREAM_INFO, iceCreamInfo})


export const requestIcecreamsComments = (iceCreamInfo, dispatch, totalCommentCount, currentPage, comments ) => {  

    

    dispatch(setIceCreamInfo(iceCreamInfo))
    dispatch(setCurrentPageAction(currentPage))
    dispatch(setTotalStoriesCount(totalCommentCount))

    dispatch(setIcecremsComment(comments))
  
}

export default commentIcecreamReducer