import React, { useState } from 'react';
import {BACKEND_URL} from '../Default/urls'
import { useNavigate, useSearchParams } from 'react-router-dom';

function NewBench() {
  const [searchParams] = useSearchParams();
  const parkId = parseInt(searchParams.get("id"));
  const [bench_title, setName] = useState('');
  const [thumbnail, setThumbnail] = useState(null);
  const [audio_binary, setAudio] = useState(null);
  const [contributor, setAudioContributor] = useState('');
  const history = useNavigate();

const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('park_id', parkId);
    formData.append('bench_title', bench_title);
    formData.append('thumbnail', thumbnail);
    formData.append('secondary_model.audio_binary', audio_binary);
    formData.append('secondary_model.contributor', contributor);
    formData.append('secondary_model.length_category', "0-5");
    formData.append('secondary_model.season_category', "SP");
    fetch(`${BACKEND_URL}/benches/create_admin_bench/`, {
      method: 'POST',
      body: formData
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

  const handleThumbnailChange = (event) => {
    setThumbnail(event.target.files[0]);
  };

  const handleAudioChange = (event) => {
    setAudio(event.target.files[0]);
  };

  const handleAudioContributorChange = (event) => {
    setAudioContributor(event.target.value);
  };

    return (
      <div>
        <div class="flex" style={{'background': 'lightgrey', 'alignItems': 'left', 'margin': '30px ', 'padding': '10px'}}>
          <form onSubmit={handleSubmit}>
          <h1>New Bench Creation</h1>
          <p>Bench Name(Required):
          <input name ="bench_title" onChange={handleNameChange} type="text" style={{'margin': '10px' ,'width': '180px'}} maxLength={30}></input>
          </p>
          <p>Thumbnail (Required):
          <input name ="thumbnail" onChange={handleThumbnailChange} type="file" style={{'margin': '10px'}}></input>
          </p>
          <p>Audio (Optional):
          <input name ="secondary_model.audio_binary" onChange={handleAudioChange} type="file" style={{'margin': '10px'}}></input>
          </p>
          <p>Audio Contributor (Optional):
          <input name ="secondary_model.contributor" onChange={handleAudioContributorChange} type="text" style={{'margin': '10px', 'width': '180px'}} maxLength={30}></input>
          </p>
          <button type="submit" onClick={handleSubmit}>Add Bench</button>
          </form>
        </div>
      </div>  
    );
  }
  
  export default NewBench;