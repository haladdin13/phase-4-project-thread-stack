import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";


// import Dashboard from "./components/Dashboard";
// import Category from "./components/Category";
// import User from "./components/User";
// import GroupThread from "./components/GroupThread";
// import Thread from "./components/Thread";
// import Post from "./components/Post";
// import Favorite from "./components/Favorite";
import Navbar from "./Navbar";



function App() {

  const [categories, setCategories] = useState([]);

  return <div>
    {/* <Route path = "/" element = {<Dashboard />} />
    <Route path = "/categories" element = {<Category categories={categories}/>} /> */}
    <Navbar />
  </div>
}

export default App;
