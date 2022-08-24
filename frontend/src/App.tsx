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

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />}></Route>
        <Route path='/weather' element= {<Weather/>}></Route>
        <Route path='/icecream' element= {<Icecream/>}></Route>
        <Route path='/icecream/:id' element={<IcecreamInfo/>}></Route>
        
      </Routes>
    </BrowserRouter>
  );
}

export default App;
