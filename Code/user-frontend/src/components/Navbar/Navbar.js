import { Link, Outlet } from "react-router-dom";
import logo from "../../assets/logo.png";
import React from 'react';

const Navbar = () => {

    return (
        <>
            <nav className="nav"
                style={{
                    position: "fixed",
                    top: "0px",
                    width: "100%",
                    display: "flex",
                    height: "80px",
                    "boxShadow": "0 0.1vw 0.5vw 0 #00000066",
                    "zIndex": 99999,
                    "backgroundColor": "#fff",
                    "alignItems": "center"
                }}
            >
                <Link to="/">
                    <img className="logo-main"
                        src={logo}
                        alt=""
                        style={{
                            display: "block",
                            "marginLeft": "auto",
                            "marginRight": "auto",
                            height: "50px",
                            "zIndex": 999999
                        }} />
                </Link>
            </nav>
            <Outlet />
        </>
    )
}

export default Navbar;