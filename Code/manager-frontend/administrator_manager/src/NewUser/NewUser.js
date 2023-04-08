import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Cookies from 'js-cookie';
import {BACKEND_URL} from '../Default/urls'

function NewUser() {
  const navigate = useNavigate();
  const [error, setError] = useState(null);

  useEffect(() => {
    const access_token = Cookies.get('access_token');
    fetch(BACKEND_URL + "/park_admin/get_admin_info/", {
      method: "GET",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${access_token}`,
      },
    })
      .then((response) => {
          return response.json();
      }).then((data) => {
        if(!data.is_superuser)
            navigate("/");
      })
      .catch((error) => {
        navigate("/login");
      });
  }, []);

  const handleSubmit = (event) => {
    event.preventDefault();
    let response;
    const formData = new FormData(event.target);
    const parsedData = {
      username: formData.get("email"),
    };


    const access_token = Cookies.get('access_token');
    // Send POST request
    fetch(BACKEND_URL+"/park_admin/create_new_admin/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${access_token}`,
      },
      credentials: 'include',
      body: JSON.stringify(parsedData),
    }).then((res) => {
        response = res;
        return res.json();
      })
      .then((data) => {
        if(response.ok){
          navigate("/");
        }
        else{
          setError(data.detail);
        }
    })};

  return (
    <div class="formDiv">
        <form onSubmit={handleSubmit}>
        <p>Email:
            <input name="email" type="email" required/>
        </p>
                
        <button type="submit">Create Account</button>
        <p style={{'color':'red'}}>{error}</p>
        </form>
    </div>
  );
}

export default NewUser;