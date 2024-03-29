import { Link } from 'react-router-dom';
import BenchList from './BenchList'
import React, { useState, useEffect } from 'react';
import {BACKEND_URL} from '../Default/urls'
import { useSearchParams } from 'react-router-dom';
import '../Default/Container.css'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faPlus, faPencil} from '@fortawesome/free-solid-svg-icons';
import { consoleWrapper} from "../Default/ConsoleWrapper"


function ParkPage() {
  const [parkTitle, setParkTitle] = useState('Loading...');
  const [searchParams] = useSearchParams();
  const parkId = parseInt(searchParams.get("id"));

  useEffect(() => {
    fetch(`${BACKEND_URL}/parks/get_all_admin_parks/`)
      .then(response => response.json())
      .then(data => {
        const bench = data.find(item => item.park_id === parkId);
        if (bench) {
          setParkTitle(bench.name);
        }
      })
      .catch(error => consoleWrapper.log(error));
  }, [parkId]);
  return (
    <div>
    <div style = {{'display': 'inline-block', 'margin-left': '100px','margin-top':'25px','margin-bottom': '25px', 'align-items': 'left'}}>
      <h1>{parkTitle}</h1>
      <FontAwesomeIcon icon={faPencil}/>
      <Link to={`/edit_park?id=${parkId}`}>Edit Park</Link>
      <br></br>
    </div>
    <div style = {{'display': 'flex', 'margin-left': '100px','align-items': 'left'}}>
    <FontAwesomeIcon icon={faPlus}/>
    <Link to={`/new_bench?id=${parkId}`}>Create new bench</Link>
  </div>
  <div>
    <BenchList />
  </div>
  
    </div>

  );
}

export default ParkPage;