import React, { useState, useEffect } from 'react';
import {BACKEND_URL} from '../Default/urls'
import Select from 'react-select';

function SearchableDropdown(props) {
  const [options, setOptions] = useState([]);

  useEffect(() => {
    fetch(`${BACKEND_URL}${'/parks/get_all_admin_parks/'}`)
      .then(response => response.json())
      .then(data => {
        const options = data.map(item => ({
          value: item.park_id,
          label: item.name
        }));
        setOptions(options);
      })
      .catch(error => console.log(error));
  }, []);

  const handleChange = selected => {
    props.onSelect(selected.value);
  };

  return (
    <div>
      <Select
        options={options}
        onChange={handleChange}
        placeholder="Select a park"
      />
    </div>
  );
}

export default SearchableDropdown;