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
        
      </Routes>
    </BrowserRouter>
  );
}

export default App;
