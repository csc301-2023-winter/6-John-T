import React, { useState, useEffect } from 'react';
import {BACKEND_URL} from '../Default/urls'
import { useNavigate, useSearchParams } from 'react-router-dom';
import Cookies from 'js-cookie';

function NewPark() {
  const [searchParams] = useSearchParams();
  const parkId = parseInt(searchParams.get("id"));
  const [park_name, setName] = useState('');
  const [park_location, setLocation] = useState(null);
  const history = useNavigate();
  
  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('park_name', park_name);
    formData.append('park_location', park_location);

    const access_token = Cookies.get('access_token');
    fetch(`${BACKEND_URL}/parks/create_admin_park/`, {
      method: 'POST',
      body: formData,
      credentials: "include",
      headers: {
        Authorization: `Bearer ${access_token}`,
      }
    })
    .then(response => {
      if (response.ok) {
        history(`/park?id=${parkId}`);
      }
    })
    .catch(error => console.log(error));
  };

  const handleName = (event) => {
    setName(event.target.value);
  };

  const handleLocation = (event) => {
    setLocation(event.target.value);
  };

    return (
        <div>
        <div className="flex" style={{'background': 'lightgrey', 'alignItems': 'left', 'margin': '30px ', 'padding': '10px'}}>
        <form onSubmit={handleSubmit}> 
          <h1>New Park Creation</h1>
          <p>Park Name(Required):
          <input name="park_name" onChange={handleName} type="text" style={{'margin': '10px' ,'width': '180px'}}></input>
          </p>
          <p>Park Location(Required):
          <input name="park_location" onChange={handleLocation} ></input>  
          </p>
          <button type="submit" >Add Park</button>
        </form>
        </div>
      </div>   
    );
  }
  
  export default NewPark;