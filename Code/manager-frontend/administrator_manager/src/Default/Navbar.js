import React, { useState, useEffect } from 'react';
import './Navbar.css';
import Cookies from 'js-cookie';
import { useNavigate , useLocation} from 'react-router-dom';
import { BACKEND_URL } from '../Default/urls';
import { consoleWrapper} from "../Default/ConsoleWrapper"

function Navbar() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isSU, setIsSU] = useState(false);
  const history = useNavigate();
  const location = useLocation();

  useEffect(() => {
    handleReload();
  }, [location.pathname]);

  const handleLogout = () => {
    Cookies.set('access_token', '');
    Cookies.set('refresh_token', '');
    setIsAuthenticated(false);
  };

  useEffect(() => {
    const access_token = Cookies.get('access_token');
    fetch(BACKEND_URL + "/park_admin/get_admin_info/", {
      method: "GET",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${access_token}`,
      },
    })
      .then((response) => {
        if (response.status === 200) {
          setIsAuthenticated(true);
          return response.json();
        } else {
          setIsAuthenticated(false);
          history("/login");
        }
      }).then((data) => {
        setIsSU(data.is_superuser);
        consoleWrapper.log(data.is_superuser)
      })
      .catch((error) => {
        setIsAuthenticated(false);
        history("/login");
      });
  }, []);
  

  const handleReload = () => { 
    const access_token = Cookies.get('access_token');
    fetch(BACKEND_URL + "/park_admin/get_admin_info/", {
      method: "GET",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${access_token}`,
      },
    })
      .then((response) => {
        if (response.status === 200) {
          setIsAuthenticated(true);
          return response.json()
        } else {
          setIsAuthenticated(false);
          history("/login");
        }
      }).then((data) => {
        setIsSU(data.is_superuser);
      })
      .catch((error) => {
        setIsAuthenticated(false);
        history("/login");
      });;};

  return (
    <div className="navbar">
      <h2 className="navbar-title">Ontario Parks Audio File Manager</h2>
      <div className="navbar-items">
        <a href="/" className="navbar-item">
          Select Park
        </a>

        {isAuthenticated && (
          <a href="/new_park" className="navbar-item">
          Create New Park
        </a>
        )}

        {isSU && (
          <a href="/new_user" className="navbar-item">
          Create New User
        </a>
        )}
        
        {isAuthenticated && (
        <a href="/profile" className="navbar-item">
          Profile
        </a>
        )}
        {isAuthenticated && (
          <a
            href="/login"
            className="navbar-item"
            onClick={handleLogout}
          >
            Logout</a>
    )}
  </div>
</div>

);
}

export default Navbar;
