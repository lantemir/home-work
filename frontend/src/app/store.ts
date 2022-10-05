import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import { combineReducers } from "redux";
import thunk from "redux-thunk";

import { GetAllMessageReducer } from '../pages/Home';
import icecreamReducer from './redux/icecream-reducer';
import commentIcecreamReducer from './redux/comment-icecream-reducer';
import chatReducer from './redux/chat-reducer';
import tokenReducer from './redux/token-reducer';

const globalReducer = combineReducers({
  GetAllMessage: GetAllMessageReducer,
  IcecreamR: icecreamReducer,
  CommentIcecreamR: commentIcecreamReducer,
  ChatR: chatReducer,
  TokenR: tokenReducer,

});

const initialState = {

  // token: localStorage.getItem("token") ? localStorage.getItem("token") : null
};



export const store = configureStore({
  reducer: globalReducer,
  devTools: true,
  // @ts-ignore
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk),
  // @ts-ignore
  preloadedState: initialState,
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
