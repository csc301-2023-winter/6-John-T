function NewPark() {
    
  
    return (
        <div>
        <div class="flex" style={{'background': 'lightgrey', 'alignItems': 'left', 'margin': '30px ', 'padding': '10px'}}>
          <h1>New Park Creation</h1>
          <p>Park Name(Required):
          <input name="park_name"  type="text" style={{'margin': '10px' ,'width': '180px'}}></input>
          </p>
          <p>Park Location(Required):
          <input name="park_location"></input>  
          </p>
          <button type="submit" >Add Park</button>
        </div>
      </div>   
    );
  }
  
  export default NewPark;