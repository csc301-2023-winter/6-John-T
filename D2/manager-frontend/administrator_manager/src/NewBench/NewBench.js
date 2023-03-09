import React from 'react';
import { Link } from 'react-router-dom';

function NewBench() {
    return (
      <div>
        <div class="flex" style={{'background': 'lightgrey', 'alignItems': 'left', 'margin': '30px ', 'padding': '10px'}}>
          <h1>New Bench Creation</h1>
          <p>Bench Name(Required):
          <input type="text" style={{'margin': '10px' ,'width': '180px'}} maxLength={30}></input>
          </p>
          <p>Thumbnail (Required):
          <input type="file" style={{'margin': '10px'}}></input>
          </p>
          <p>Audio (Optional):
          <input type="file" style={{'margin': '10px'}}></input>
          </p>
          <p>Audio Contributor (Optional):
          <input type="text" style={{'margin': '10px', 'width': '180px'}} maxLength={30}></input>
          </p>
          <Link to="/park">Add Bench</Link>
        </div>
      </div>  
    );
  }
  
  export default NewBench;