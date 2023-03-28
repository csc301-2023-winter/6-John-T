function EditPark() {
    
  
    return (
        <div>
        <div class="flex" style={{'background': 'lightgrey', 'alignItems': 'left', 'margin': '30px ', 'padding': '10px'}}>
          <h1>Update Park</h1>
          <p>Bench Name:
          <input name="park_name"  type="text" style={{'margin': '10px' ,'width': '180px'}}></input>
          </p>
          <p>Park Location:
          <input name="park_location"></input>  
          </p>
          <button type="submit" >Update Park</button>
        </div>
      </div>  
    );
  }
  
  export default EditPark;