import React, { useState, useEffect } from 'react';
import {BACKEND_URL} from '../Default/urls'
import { useSearchParams } from 'react-router-dom';
import '../Default/Container.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faPencil, faArrowsRotate, faTrash, faEraser, faDownload} from '@fortawesome/free-solid-svg-icons';

function BenchList() {

  const [benches, setBenches] = useState([]);
  const [searchParams] = useSearchParams();
  useEffect(() => {
    fetch(`${BACKEND_URL}${'/benches/get_all_admin_benches/'}${searchParams.get("id")}${'/'}`)
      .then(response => response.json())
      .then(data => {
        const benches = data.map(item => ({
          audio: item.audio_details.audio_file,
          bench_id: item.bench_id,
          bench_title: item.bench_title,
          qr_code: item.qr_code,
          thumbnail: item.thumbnail,
          contributor: item.audio_details.contributor
        }));
        setBenches(benches);
      })
      .catch(error => console.log(error));
  }, []);


  return (
    <div class = 'container'>
      {benches.map((bench) => (

<div  style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)",  gap: "10px", padding: "10px", borderBottom: "1px solid #000000" }}>
          <div style={{ gridColumn: "1 / 2", gridRow: "1 / 2" }}><h2>{bench.bench_title}</h2></div>
          <div style={{ gridColumn: "1 / 2", gridRow: "2 / 3" }}>Contributor: {bench.contributor}</div>
          <div style={{ gridColumn: "1 / 2", gridRow: "3 / 4" }}>
            <audio controls>
              <source src={BACKEND_URL+bench.audio} type="audio/mpeg" />
            </audio>
          </div>
          <div style={{ gridColumn: "2 / 3", gridRow: "1 / 4" }}>
            <img src={BACKEND_URL+bench.thumbnail} style={{ height: "200px", width: "200px"}} />
          </div>
          <div style={{ gridColumn: "3 / 4", gridRow: "3 / 4" }}>
            <FontAwesomeIcon icon={faDownload}/>
            <a href={BACKEND_URL+bench.qr_code}>Download QR code</a>
          </div>
          <div style={{ gridColumn: "4 / 5", gridRow: "3 / 4" }}>
            <FontAwesomeIcon icon={faPencil}/>
            <a href="#">Edit Bench</a>
          </div>
        </div>
    
      ))}
      </div> );
}

export default BenchList;