import React, { useEffect, useState } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import UserContext from "./UserContext";

import User from "./User"
import Dashboard from "./Dashboard";
import Category from "./Category";
import CurrentCategory from "./category_components/CurrentCategory";
import CurrentThread from "./Dashboard_components/CurrentThread";
// import GroupThread from "./components/GroupThread";
// import Thread from "./components/Thread";
// import Post from "./components/Post";
// import Favorite from "./components/Favorite";
import Navbar from "./Navbar";
import UserSignup from "./UserSignup";
import UserLogin from "./UserLogin"



function App() {

const [currentUser, setCurrentUser] = useState({})

 useEffect(()=> {
    const userInSession = sessionStorage.getItem('currentUser')
    if (userInSession){
      const user = JSON.parse(userInSession)
      setCurrentUser(user)
    }
  }, [])
  


  return (
    <>
     
      <UserContext.Provider value={{currentUser, setCurrentUser}}>
      <div className="container">
        <Routes>
          <Route path='/' element={<Dashboard />} />
          <Route path='/dashboard' element={<Dashboard />} />
          <Route path='/categories' element={<Category />} />
          <Route path="/categories/:id" element={<CurrentCategory />} />
          <Route path='/user' element={<User />} />
          <Route path='/threads/:id' element={<CurrentThread />}/>
          <Route path='/signup' element={<UserSignup />} />
          <Route path='/login' element={<UserLogin />} />
        </Routes>
      </div>
      </UserContext.Provider>
    </>
  )

}

export default App;