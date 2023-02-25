import React from 'react';
import SearchableDropdown from './SearchableDropdown'
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div style = {{'display': 'flex', 'padding': '20px', 'justify-content': 'center', 'align-items': 'center'}}>
        <SearchableDropdown />
        <button style = {{'display': 'flex', 'margin-left': '40px', 'margin-top': '10px'}}><Link to="/assignment-2-6-3-gaomich4-harishan/park" style={{'text-decoration':'none', 'color':'#000000'}}>
          Select Park</Link></button>
    </div>

  );
}

export default HomePage;