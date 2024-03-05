import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";


import Dashboard from "./components/Dashboard";
import Category from "./components/Category";
import User from "./components/User";
import GroupThread from "./components/GroupThread";
import Thread from "./components/Thread";
import Post from "./components/Post";
import Favorite from "./components/Favorite";



function App() {

  const [categories, setCategories] = useState([]);

  <div>
    <Route path = "/" element = {<Dashboard />} />
    <Route path = "/categories" element = {<Category categories={categories}/>} />
  </div>
}

export default App;
