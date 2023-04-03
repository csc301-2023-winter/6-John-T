import React, { useState} from 'react';
import {BACKEND_URL} from '../Default/urls'
import { useNavigate, useSearchParams } from 'react-router-dom';
import Cookies from 'js-cookie';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faTrash} from '@fortawesome/free-solid-svg-icons';

function EditPark() {
  const [park_name, setName] = useState('');
  const [searchParams] = useSearchParams();
  const parkId = parseInt(searchParams.get("id"));
  const [park_location, setLocation] = useState('');
  const history = useNavigate();
  const access_token = Cookies.get('access_token');

const handleDeletepark = (event) => {event.preventDefault();

    fetch(`${BACKEND_URL}/parks/delete_admin_park/${parkId}/`, {
        method: 'DELETE',
        credentials: "include",
        headers: {
        Authorization: `Bearer ${access_token}`,
      }
      })
      .then(response => {
        if (response.ok) {
          history(`/`);
        }
      })
      .catch(error => console.log(error));
}


const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('name', park_name);
    formData.append('location', park_location);
    fetch(`${BACKEND_URL}/parks/update_admin_park/${parkId}/`, {
      method: 'PUT',
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

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  const handlelocationChange = (event) => {
    setLocation(event.target.value);
  };

  
    return (
        <div class="formDiv">       
          <h1>Update Park</h1>
          <p>Park Name:
          <input name="park_name"  type="text" style={{'margin': '10px' ,'width': '180px'}} onChange={handleNameChange}></input>
          </p>
          <p>Park Location:
          <input name="park_location" onChange={handlelocationChange}></input>  
          </p>
          <button type="submit" onClick={handleSubmit}>Update Park</button>
          
          <p><button style={{'color':'red'}} onClick={handleDeletepark}><b><FontAwesomeIcon icon={faTrash}/>Delete Park</b></button></p>       
      </div>  
    );
  }
  
  export default EditPark;