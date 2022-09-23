import { configureStore, ThunkAction, Action, getDefaultMiddleware } from '@reduxjs/toolkit';
import { combineReducers } from "redux";
import thunk from "redux-thunk";

import { GetAllMessageReducer } from '../pages/Home';
import icecreamReducer from './redux/icecream-reducer';
import commentIcecreamReducer from './redux/comment-icecream-reducer';
import chatReducer from './redux/chat-reducer';

const globalReducer = combineReducers({
  GetAllMessage: GetAllMessageReducer,
  IcecreamR: icecreamReducer,
  CommentIcecreamR: commentIcecreamReducer,
  ChatR: chatReducer,
});

const initialState = {

};



export const store = configureStore({
  reducer: globalReducer,
  devTools: true,
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk),
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
