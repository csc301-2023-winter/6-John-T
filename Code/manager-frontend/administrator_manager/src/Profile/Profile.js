import React, { useState, useEffect } from 'react';
import Cookies from 'js-cookie';
import { useNavigate } from 'react-router-dom';
import { BACKEND_URL } from '../Default/urls';
import validator from 'validator'

function Profile() {
  const [email, setEmail] = useState(null);
  // change after park is implemented
  // const [park, setPark] = useState(null);
  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmNewPassword, setConfirmNewPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const history = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    if (newPassword !== confirmNewPassword) {
      setErrorMessage('The new passwords do not match.');
      return;
    }

    if (!validator.isStrongPassword(newPassword, {
        minLength: 8, minLowercase: 1,
        minUppercase: 1, minNumbers: 1, 
        minSymbols: 0, returnScore: false,
      })) {
        setErrorMessage('Password needs to be at least 8 characters, with a number, uppercase letter, and lowercase letter.')
        return;
      }
      

    // Proceed with form submission, e.g., send data to the server
    const parsedData = {
      username: email,
      old_password: oldPassword,
      new_password: newPassword,
      confirm_password: confirmNewPassword,
    };

    const access_token = Cookies.get('access_token');
    // Send POST request
    fetch(BACKEND_URL+"/park_admin/update_admin_info/", {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${access_token}`,
      },
      credentials: 'include',
      body: JSON.stringify(parsedData),
    }).then(response => {
      response.json().then(data => {
        if(response.ok){
          Cookies.set('access_token', '');
          Cookies.set('refresh_token', '');
          history("/login");
        }else {
          setErrorMessage(data.message);
          return;
        }
      });
      })
  };

  useEffect(() => {
    const access_token = Cookies.get('access_token');
    fetch(BACKEND_URL + "/park_admin/get_admin_info/", {
      method: "GET",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${access_token}`,
      },
    }).then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        setEmail(data.username);
        //remove after implementing manages park
        //setPark(data.manages_park);
      })
      .catch((error) => {
        history("/login");
      });
  }, []);

  return (
    <div class="formDiv">
        <p>Your Email: {email}</p>
        {/* Once manages_park is implemented, add later */}

        {/* {park != null && (
          <p>Your park: {park}</p>
        )} */}
        <h2>Change your Password</h2>
        <form onSubmit={handleSubmit}>
        <p>
          <label htmlFor="oldPassword">Old Password:</label>
          <input
            type="password"
            id="oldPassword"
            value={oldPassword}
            onChange={(e) => setOldPassword(e.target.value)}
            required
          />
        </p>
        <p>
          <label htmlFor="newPassword">New Password:</label>
          <input
            type="password"
            id="newPassword"
            value={newPassword}
            onChange={(e) => setNewPassword(e.target.value)}
            required
          />
        </p>
        <p>
          <label htmlFor="confirmNewPassword">Confirm New Password:</label>
          <input
            type="password"
            id="confirmNewPassword"
            value={confirmNewPassword}
            onChange={(e) => setConfirmNewPassword(e.target.value)}
            required
          />
        </p>
        {errorMessage && <p style={{'color':'red'}}>{errorMessage}</p>}
        <button type="submit">Change Password</button>
      </form>
    </div>
  );
}

export default Profile;