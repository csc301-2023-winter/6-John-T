import React, { useState, useEffect } from 'react';
import {BACKEND_URL} from '../Default/urls'
import Select from 'react-select';
import { consoleWrapper} from "../Default/ConsoleWrapper"

function SearchableDropdown(props) {
  const [options, setOptions] = useState([]);

  const styles = {
    control: (base, state) => ({
      ...base,
      background: "rgb(196, 181, 155)",
    }),
    menu: base => ({
      ...base,
      borderRadius: 0,
      marginTop: 0,
      background: "rgb(196, 181, 155)",
      color: "rgb(96, 81, 55)",
    }),
    placeholder: base => ({
      ...base,
      color: "#241F21"
    })
  }

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
      .catch(error => consoleWrapper.log(error));
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
        styles={styles}
      />
    </div>
  );
}

export default SearchableDropdown;