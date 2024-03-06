import React, { useImperativeHandle } from 'react';
import { Link, useMatch, useResolvedPath } from "react-router-dom"

function Navbar(){
    return (<nav className="nav">
        <Link to='/' className="site-title">
            Thread Stack
        </Link>
        <ul>
           <CustomLink to="/dashboard">Dashboard</CustomLink>
           <CustomLink to="/category">Categories</CustomLink>
           <CustomLink to="/user">User</CustomLink>  
        </ul>
    </nav>
    )
}

function CustomLink({to, children, ...props }){
    const resolvedPath = useResolvedPath(to)
    const isActive = useMatch({ path: resolvedPath.pathname })
    return(
        <li className={isActive === to ? "active" : ""}>
            <Link to={to} {...props}>
                {children}
            </Link>
        </li>
    )
}

export default Navbar;