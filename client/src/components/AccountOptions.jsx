import React, {useState, useEffect} from "react";
import { useUser } from "./UserContext.jsx";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom"
import "./AccountOptionsStyles.css"

function AccountOptions() {

    const {currentUser, setCurrentUser} = useUser();
    const [isOpen, setIsOpen] = useState(false);

    const navigate = useNavigate();
    const toggleMenu = () => setIsOpen(!isOpen);

    const loggingOut = () => {

        fetch(`http://localhost:5555/logout`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(res => res.json())
        .then(data => {
             console.log(data)
             sessionStorage.removeItem('currentUser')
             setCurrentUser({})
             navigate('/login')
        })
    }



    function isLoggedIn() {
        if (currentUser) {
            return (
                <div>
                    <button onClick={loggingOut}>
                        <Link to="/logout">Logout</Link>
                    </button>
                </div>
            )
        } else {
            return (
                <div>
                    <button>
                        <Link to="/login">Login</Link>
                    </button>
                    <button>
                        <Link to="/signup">Sign Up</Link>
                    </button>
                </div>
            )
        }
    }



    return (
        <div>
            <button onClick={toggleMenu} className="avatar-button" >
                <img src={currentUser?.pictureUrl || 'default-picture.png'} alt="User Picture" className="user-Picture" />
            </button>

            {isOpen && (
                <div className="dropdown-menu">
                    <div className="dropdown-menu-header">
                        <div className="dropdown-menu-header-title">
                            <h3>Account</h3>
                            <p>{currentUser.user_name} is threading!</p>
                        </div>
                        <div className="dropdown-menu-header-close" onClick={toggleMenu}>
                            <i className="fas fa-times"></i>
                        </div>
                    </div>
                    <div className="dropdown-menu-body">
                        {isLoggedIn()}
                    </div>
                </div>
            )}
        </div>
    )
}

export default AccountOptions;