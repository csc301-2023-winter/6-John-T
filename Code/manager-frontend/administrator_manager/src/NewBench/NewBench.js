import React, { useState } from 'react';
import {BACKEND_URL} from '../Default/urls'
import { useNavigate, useSearchParams } from 'react-router-dom';
import Cookies from 'js-cookie';
import { consoleWrapper} from "../Default/ConsoleWrapper"

function NewBench() {
  const [searchParams] = useSearchParams();
  const parkId = parseInt(searchParams.get("id"));
  const [bench_title, setName] = useState('');
  const [thumbnail, setThumbnail] = useState(null);
  const [audio_file, setAudio] = useState(null);
  const [contributor, setAudioContributor] = useState('');
  const history = useNavigate();

const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('park_id', parkId);
    formData.append('bench_title', bench_title);
    formData.append('thumbnail', thumbnail);
    formData.append('secondary_model.audio_file', audio_file);
    formData.append('secondary_model.contributor', contributor);
    formData.append('secondary_model.length_category', '0-5');
    formData.append('secondary_model.season_category', 'SP');

    const access_token = Cookies.get('access_token');
    fetch(`${BACKEND_URL}/benches/create_admin_bench/`, {
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
    .catch(error => consoleWrapper.log(error));
  };

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  const handleThumbnailChange = (event) => {
    setThumbnail(event.target.files[0]);
    consoleWrapper.log(thumbnail);
  };

  const handleAudioChange = (event) => {
    setAudio(event.target.files[0]);
    consoleWrapper.log(audio_file);
  };

  const handleAudioContributorChange = (event) => {
    setAudioContributor(event.target.value);
  };

    return (
      <div>
        <div class="formDiv">
          <form onSubmit={handleSubmit}>
          <h1>New Bench Creation</h1>
          <p>Bench Name(Required):
          <input required name ="bench_title" onChange={handleNameChange} type="text" style={{'margin': '10px' ,'width': '180px'}} maxLength={30}></input>
          </p>
          <p>Thumbnail (Required):
          <input required name ="thumbnail" onChange={handleThumbnailChange} type="file" accept="image/png, image/jpeg" style={{'margin': '10px'}}></input>
          </p>
          <p>Audio (Optional):
          <input name ="audio_file" onChange={handleAudioChange} type="file" accept="audio/mpeg" style={{'margin': '10px'}}></input>
          </p>
          <p>Audio Contributor (Optional):
          <input name ="contributor" onChange={handleAudioContributorChange} type="text" style={{'margin': '10px', 'width': '180px'}} maxLength={30}></input>
          </p>
          <button type="submit" >Add Bench</button>
          </form>
        </div>
      </div>  
    );
  }
  
  export default NewBench;