import React from 'react';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import HomePage from './ParkList/HomePage';
import ParkPage from './BenchList/ParkPage';
import Navbar from './Default/Navbar';
import NewBench from './NewBench/NewBench';

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