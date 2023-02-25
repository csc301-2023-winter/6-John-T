import React from 'react';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import HomePage from './HomePage';
import ParkPage from './ParkPage';
import Navbar from './Navbar';
import NewBench from './NewBench';

function App() {
  return (
      <div>
        <Navbar/>
        <Routes>
          <Route exact path="/assignment-2-6-3-gaomich4-harishan" element={<HomePage />} />
          <Route path="/assignment-2-6-3-gaomich4-harishan/park" element={<ParkPage />} />
          <Route path="/assignment-2-6-3-gaomich4-harishan/new_bench" element={<NewBench />} />
        </Routes>
      </div>
  );
}

export default App;