import React from 'react';
import './Navbar.css';

function Navbar() {
  return (
    <div className="navbar">
      <h2 className="navbar-title">Ontario Parks Audio File Manager</h2>
      <div className="navbar-items">
        <a href="/" className="navbar-item">Select Park</a>
      </div>
    </div>
  );
}

export default Navbar;