import React from 'react';
import { Link } from 'react-router-dom';
import BenchList from './BenchList'

function ParkPage() {
  return (
    <div>
    <div style = {{'display': 'flex', 'margin-left': '100px','margin-top':'25px','margin-bottom': '25px', 'align-items': 'left'}}>
      <h1>Arrowhead Provincial Park</h1>
      <br></br>
    </div>
    <div style = {{'display': 'flex', 'margin-left': '100px','align-items': 'left'}}>
    <Link to="/new_bench">Create new bench</Link>
  </div>
  <div>
    <BenchList />
  </div>
  
    </div>

  );
}

export default ParkPage;