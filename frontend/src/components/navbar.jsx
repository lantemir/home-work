import React from 'react'
import { NavLink } from 'react-router-dom'

export function Navbar1() {
  return (
    <div>     
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
    <div className="container-fluid">
      <a className="navbar-brand" href="#">Navbar</a>
      <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav">
          <li className="nav-item">            
            <NavLink to="/" className="nav-link active" >Home</NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/weather" className="nav-link nav-custom2" >Погода</NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/icecream" className="nav-link nav-custom2" >Мороженное</NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/timer" className="nav-link nav-custom2" >Таймер</NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/calculator" className="nav-link nav-custom2" >Калькулятор</NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/jsonplaceholder" className="nav-link nav-custom2" >Json Placeholder</NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/mylist" className="nav-link nav-custom2" >mylist Class</NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/chat" className="nav-link nav-custom2" >чат</NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/emailsender" className="nav-link nav-custom2" >email</NavLink>
          </li>
    
          
        </ul>
      </div>
    </div>
  </nav>
  </div>
    
  )
}

