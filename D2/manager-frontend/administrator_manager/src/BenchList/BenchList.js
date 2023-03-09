import React from 'react';
import '../Default/Container.css'

function BenchList() {
  const benches = [    { title: 'Arrowhead Lake Bench', author: 'Paula Vital', audio: "audio/audio1.mp3"}, {title:'Mayflower Lake Bench', author:'Paula Vital', audio: "audio/audio2.mp3"}];

  return (
    <div class = 'container'>
      {benches.map((bench) => (

<div  style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)",  gap: "10px", padding: "10px", borderBottom: "1px solid #000000" }}>
          <div style={{ gridColumn: "1 / 2", gridRow: "1 / 2" }}><h2>{bench.title}</h2></div>
          <div style={{ gridColumn: "1 / 2", gridRow: "2 / 3" }}>Contributor: {bench.author}</div>
          <div style={{ gridColumn: "1 / 2", gridRow: "3 / 4" }}>
            <audio controls>
              <source src={bench.audio} type="audio/mpeg" />
            </audio>
          </div>
          <div style={{ gridColumn: "2 / 3", gridRow: "1 / 2" }}>
            <a href="#">Edit contributor</a>
          </div>
          <div style={{ gridColumn: "2 / 3", gridRow: "2 / 3" }}>
            <a href="#">Change audio</a>
          </div>
          <div style={{ gridColumn: "2 / 3", gridRow: "3 / 4" }}>
            <a href="#">Delete audio</a>
          </div>
          <div style={{ gridColumn: "3 / 4", gridRow: "3 / 4" }}>
            <a href="#">Download QR code</a>
          </div>
          <div style={{ gridColumn: "4 / 5", gridRow: "3 / 4" }}>
            <a href="#">Delete Bench</a>
          </div>
        </div>
    
      ))}
      </div> );
}

export default BenchList;