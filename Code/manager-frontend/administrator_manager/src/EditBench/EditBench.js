import React, { useState, useEffect } from 'react';
import {BACKEND_URL} from '../Default/urls'
import { useNavigate, useSearchParams } from 'react-router-dom';
import Cookies from 'js-cookie';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faTrash} from '@fortawesome/free-solid-svg-icons';
import { consoleWrapper} from "../Default/ConsoleWrapper"

function EditBench() {
  const [old_audio, setOldAudio] = useState(null);
  const [searchParams] = useSearchParams();
  const benchId = parseInt(searchParams.get("id"));
  const [bench_title, setName] = useState('');
  const [thumbnail, setThumbnail] = useState(new File([], '', {type: 'image/jpeg'}));
  const [audio_file, setAudio] = useState(null);
  const [contributor, setAudioContributor] = useState('');
  const parkId = parseInt(searchParams.get("parkid"));
  const history = useNavigate();
  const access_token = Cookies.get('access_token');

  useEffect(() => {
    fetch(`${BACKEND_URL}${'/benches/get_admin_bench/'}${searchParams.get("id")}${'/'}`, {
      credentials: "include",
      headers: {
        Authorization: `Bearer ${access_token}`,
      }
    })
      .then(response => response.json())
      .then(data => {
        if (data.audio_details.audio_file != null){fetch(`${BACKEND_URL}${data.audio_details.audio_file}`).then(response => response.blob())
        .then(blob => {
          const old_audio = new File([blob], 'audio.mp3', {type: 'audio/mpeg'});
          setOldAudio(old_audio);
        })
        .catch(error => {
          consoleWrapper.error('Error retrieving audio file:', error);
        });}
      })
      .catch(error => consoleWrapper.log(error));
  }, []);

const handleDeleteBench = (event) => {event.preventDefault();

    fetch(`${BACKEND_URL}/benches/delete_admin_bench/${benchId}/`, {
        method: 'DELETE',
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
}

const handleDeleteAudio = (event) => {event.preventDefault();
    const formData = new FormData();
    formData.append('bench_title', '');
    formData.append('thumbnail', new File([], '', {type: 'image/jpeg'}));
    formData.append('secondary_model.audio_file', '');

    formData.append('secondary_model.contributor', '');
    formData.append('secondary_model.length_category', '');
    formData.append('secondary_model.season_category', '');
    fetch(`${BACKEND_URL}/benches/update_admin_bench/${benchId}/`, {
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
    .catch(error => consoleWrapper.log(error));}
const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('bench_title', bench_title);
    formData.append('thumbnail', thumbnail);
    if (audio_file != null){
        formData.append('secondary_model.audio_file', audio_file);
    } else{
        formData.append('secondary_model.audio_file', old_audio);
    }
    formData.append('secondary_model.contributor', contributor);
    formData.append('secondary_model.length_category', '');
    formData.append('secondary_model.season_category', '');
    fetch(`${BACKEND_URL}/benches/update_admin_bench/${benchId}/`, {
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
          <h1>Update Bench</h1>
          <p>Bench Name:
          <input name ="bench_title" onChange={handleNameChange} type="text" style={{'margin': '10px' ,'width': '180px'}} maxLength={30}></input>
          </p>
          <p>Thumbnail:
          <input name ="thumbnail" onChange={handleThumbnailChange} type="file" accept="image/png, image/jpeg" style={{'margin': '10px'}}></input>
          </p>
          <p>Audio:
          <input name ="audio_file" onChange={handleAudioChange} type="file" accept="audio/mpeg" style={{'margin': '10px'}}></input>
          <button type="submit" onClick={handleDeleteAudio}><FontAwesomeIcon icon={faTrash}/>Delete Current Audio</button>
          </p>
          <p>Audio Contributor:
          <input name ="contributor" onChange={handleAudioContributorChange} type="text" style={{'margin': '10px', 'width': '180px'}} maxLength={30}></input>
          </p>
          <button type="submit" onClick={handleSubmit}>Update Bench</button>
          <p><button style={{'color':'red'}} onClick={handleDeleteBench}><b><FontAwesomeIcon icon={faTrash}/>Delete Bench</b></button></p>

          </form>
        </div>
      </div>  
    );
  }
  
  export default EditBench;