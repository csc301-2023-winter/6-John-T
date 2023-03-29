import React, { useState } from 'react';
import SearchableDropdown from './SearchableDropdown'
import { useNavigate } from 'react-router-dom';


function HomePage() {
  const [selectedParkId, setSelectedParkId] = useState(null);
  const history = useNavigate();


  const handleParkSelect = parkId => {
    setSelectedParkId(parkId);
  };

  const handleButtonClick = () => {
    history(`/park?id=${selectedParkId}`);
  };

  return (
    <div style = {{'display': 'flex', 'padding': '20px', 'justifyContent': 'center', 'alignItems': 'center'}}>
        <SearchableDropdown onSelect={handleParkSelect} />
      {selectedParkId && (
          <button onClick={handleButtonClick} style = {{'display': 'flex', 'margin-left': '40px', 'margin-top': '10px'}}>Select Park</button>
      )}

    </div>

  );
}

export default HomePage;