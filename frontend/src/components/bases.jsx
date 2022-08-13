 import React from 'react'
 import * as navbars from '../components/navbar'
 import * as footers from '../components/footer'

export function Base1({children}) {
  return (
    <div>
        <navbars.Navbar1></navbars.Navbar1>
        <main>
             {children}
        </main>        
        <footers.Footer1></footers.Footer1>
    </div> 
  )
}

