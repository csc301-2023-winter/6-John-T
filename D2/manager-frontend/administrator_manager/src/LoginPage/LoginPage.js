import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Cookies from 'js-cookie';
import {BACKEND_URL} from '../Default/urls'

function LoginPage() {
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
        if (response.status === 200) {
          navigate("/");
        }
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
      password: formData.get("password"),
    };

    // Send POST request
    fetch(BACKEND_URL+"/api/token/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: 'include',
      body: JSON.stringify(parsedData),
    })
    .then((res) => {
      response = res;
      return res.json();
    })
    .then((data) => {
      // If the request was successful, save the tokens and navigate to the home page
      if(response.ok){
        Cookies.set('access_token', data.access);
        Cookies.set('refresh_token', data.refresh, { httpOnly: true });
        navigate("/");
      }
      else if(response.status === 401){
        setError('Email/Password is incorrect');
      }
      else{
        console.log(data.response);
      }
    });
  };

  return (
    <div style={{'background': 'lightgrey', 'display':'flex','margin': '30px ', 'padding': '10px'}}>
        <form onSubmit={handleSubmit}>
        <p>Email:
            <input name="email" type="email" required/>
        </p>
        <p>Password:
            <input name="password" type="password" required/>
        </p>
                
        <button type="submit">Login</button>
        <p style={{'color':'red'}}>{error}</p>
        </form>
    </div>
  );
}

export default LoginPage;