import React, {useEffect,} from 'react';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import HomePage from './ParkList/HomePage';
import ParkPage from './BenchList/ParkPage';
import Navbar from './Default/Navbar';
import NewBench from './NewBench/NewBench';
import EditBench from './EditBench/EditBench'
import LoginPage from './LoginPage/LoginPage'
import Profile from './Profile/Profile'
import NewUser from './NewUser/NewUser'
import NewPark from './NewPark/NewPark'
import EditPark from './EditPark/EditPark'



function App() {

  return (
      <div>
        <Navbar/>
        <Routes>
          <Route exact path="/" element={<HomePage />} />
          <Route path="/park" element={<ParkPage />} />
          <Route path="/new_bench" element={<NewBench />} />
          <Route path="/edit_bench" element={<EditBench />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/new_user" element={<NewUser />} />
          <Route path="/new_park" element={<NewPark />} />
          <Route path="/edit_park" element={<EditPark />} />
        </Routes>
      </div>
  );
}

export default App;