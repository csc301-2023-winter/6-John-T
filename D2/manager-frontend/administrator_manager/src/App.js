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
          <Route exact path="/" element={<HomePage />} />
          <Route path="/park" element={<ParkPage />} />
          <Route path="/new_bench" element={<NewBench />} />
        </Routes>
      </div>
  );
}

export default App;