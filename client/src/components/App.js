import React, { useEffect, useState } from "react";
import { Switch, Route, Routes } from "react-router-dom";
import UserContext from "./UserContext";


import Dashboard from "./Dashboard";
import Category from "./Category";
import User from "./User";
import CurrentCategory from "./category_components/CurrentCategory";
import CurrentThread from "./Dashboard_components/CurrentThread";
// import GroupThread from "./components/GroupThread";
// import Thread from "./components/Thread";
// import Post from "./components/Post";
// import Favorite from "./components/Favorite";
import Navbar from "./Navbar";
import UserSignup from "./UserSignup";



function App() {

  const [user, setUser] = useState({
    userName: "nkhattak",
    userAvatar: "https://bootdey.com/img/Content/avatar/avatar1.png",
  })


  return (
    <>
      <Navbar />
      <UserContext.Provider value={user}>
      <div className="container">
        <Routes>
          <Route path='/' element={<Dashboard />} />
          <Route path='/dashboard' element={<Dashboard />} />
          <Route path='/categories' element={<Category />} />
          <Route path="/categories/:id" element={<CurrentCategory />} />
          <Route path='/user' element={<User />} />
          <Route path='/threads/:id' element={<CurrentThread />}/>
          <Route path='/signup' element={<UserSignup />} />
        </Routes>
      </div>
      </UserContext.Provider>
    </>
  )

}

export default App;