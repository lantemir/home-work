import React from 'react';
import logo from './logo.svg';

import{
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import './App.css';
import './css/bootstrap/bootstrap.min.css';
import {Home} from './pages/Home';
import {Weather} from './pages/Weather';
import Icecream from './pages/Icecream';
import IcecreamInfo from './pages/IcecreamInfo';
import Timer from './pages/Timer';
import Calculator from './pages/Calculator';
import Jsonplaceholder from './pages/Jsonplaceholder';
import Mylistclass from './pages/Mylistclass';
import Chat from './pages/Chat';
import EmailSender from './pages/EmailSender';
import Login from './pages/Login';
import Register from './pages/Register';

import PictureDownload from './pages/PictureDownload';
import CeleryRedis from './pages/Celery';


// import { AuthProvider } from './context/AuthContext'; //для токена

function App() {
  return (

  
    <BrowserRouter>
    
      <Routes>
      
        <Route path='/' element={<Home />}></Route>
        <Route path='/weather' element= {<Weather/>}></Route>
        <Route path='/icecream' element= {<Icecream/>}></Route>
        <Route path='/icecream/:id' element={<IcecreamInfo/>}></Route>
        <Route path='/timer' element={<Timer/>}></Route>
        <Route path='/calculator' element={<Calculator/>}></Route>
        <Route path='/jsonplaceholder' element={<Jsonplaceholder/>}></Route>
        <Route path='/mylist' element={<Mylistclass/>}></Route>
        <Route path='/chat' element={<Chat/>}></Route>
        <Route path='/emailsender' element={<EmailSender/>} ></Route>
        <Route path='/login' element={<Login/>} ></Route>
        <Route path='/register' element={<Register/>} ></Route>
        <Route path='/downloadpicture' element={<PictureDownload/>} ></Route>
        <Route path='/celerytest' element={<CeleryRedis/>} ></Route>      

     
      </Routes>
      
    </BrowserRouter>
   
  );
}

export default App;
