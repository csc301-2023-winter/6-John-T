import React, { useState } from 'react';
import Select from 'react-select';

const options = [
  { value: 'arrowhead-park', label: 'Arrowhead Provincial Park' },
];

const SearchableDropdown = () => {
  const [selectedOption, setSelectedOption] = useState(null);

  const handleChange = (selectedOption) => {
    setSelectedOption(selectedOption);
  };

  return (
    <div>
      <Select
        options={options}
        value={selectedOption}
        onChange={handleChange}
        isSearchable={true}
        placeholder="Select a park..."
      />
    </div>
  );
};

export default SearchableDropdown;