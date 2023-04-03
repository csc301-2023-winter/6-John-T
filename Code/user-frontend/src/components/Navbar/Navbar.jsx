import { Link, Outlet, useNavigate } from "react-router-dom";
import './Navbar.css';
import { useContext, useState, useEffect } from "react";
import logo from '../../assets/logo.png';

const Navbar = () => {

    return (
        <>
            <nav className="nav">
                <Link to="/">
                    <img className="logo-main" src={logo} alt="" />
                </Link>
            </nav>
            <Outlet />
        </>
    )
}

export default Navbar;