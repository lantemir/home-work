import React, {useContext} from 'react'
import { useDispatch } from 'react-redux'
import { NavLink } from 'react-router-dom'
import { requestDeleteToken } from '../app/redux/token-reducer'
// import AuthContext from '../context/AuthContext'

export function Navbar1() {

  // let {name} = useContext(AuthContext)
  const token = localStorage.getItem('tokenHomeWork')
  const dispatch = useDispatch()

  const logout = () => {
    requestDeleteToken(dispatch)
  }


  return (
    <div>     
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
    <div >
      <a className="navbar-brand" href="#">Navbar</a>
    
      <div className="" id="navbarNav">
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
          {/* <li className="nav-item">
            <NavLink to="/chat" className="nav-link nav-custom2" >чат</NavLink>
          </li> */}
          <li className="nav-item">
            <NavLink to="/emailsender" className="nav-link nav-custom2" >email</NavLink>
          </li>
          <li className="nav-item">
            <a href='/rooms' className="nav-link nav-custom2" >чат2.0</a>
          </li>
          {token ? 
          <li className="nav-item">
            <NavLink to="/login" className="nav-link nav-custom2" onClick={logout} >выйти</NavLink>
          </li> :
          <div>
            <li className="nav-item">
            <NavLink to="/login" className="nav-link nav-custom2" >логин</NavLink>
            </li>
            <li className="nav-item">
            <NavLink to="/register" className="nav-link nav-custom2" >регистрация</NavLink>
            </li>
           </div>         
          }
          {/* <li className="nav-item">
            <NavLink to="/login" className="nav-link nav-custom2" >логин</NavLink>
          </li> */}
          {/* <li className="nav-item">
            <NavLink to="/register" className="nav-link nav-custom2" >регистрация</NavLink>
          </li> */}

          <li className="nav-item">
            <NavLink to="/downloadpicture" className="nav-link nav-custom2" >Скачиваем картинки</NavLink>
          </li>
          
        </ul>
      </div>
    </div>
  </nav>
  </div>
    
  )
}

