import React, {useContext, useEffect, useState} from "react";



async function addSong(credentials)
  {
  
    return fetch("http://localhost:8086/songs",
    {
      mode: 'no-cors',
      method: 'POST',
    body: JSON.stringify(credentials)
    }).then(console.log(credentials));
    
  }

async function addArtist(credentials)
  {
    return fetch("http://localhost:8086/artists",
    {
      mode: 'no-cors',
      method: 'POST',
    body: JSON.stringify(credentials)
    }).then(console.log(credentials));
    
    
  
  }
  function AddForm()
  {
    const [title, setTitle] = useState('');
    const [gen, setGen] = useState('');
    const [anAparitie, setAn] = useState('');
    const[name, setName] = useState('');
    const [isActive, setActive]=useState('');

    const handleSubmit = async e =>{
      e.preventDefault();
      
      const response_song = await addSong({
        title, 
        gen,
        anAparitie
      });
      const response_artist = await addArtist({
        name,
        isActive
      });
      
    }

    useEffect(()=>{
      handleSubmit()
    }, [])
   

    return(
        <div id ="login-form">
        <form onSubmit={handleSubmit}>
        <label>
          <h1>New song and artist</h1>
          <br></br>
          Title: 
          <input id ="title" name = "title" type= "text"
          value={title} onChange={
            (e)=> setTitle(e.target.value)}>




            </input>
              Gen muzical:
              <br></br>
            <input id ="gen" name = "gen" type= "text"
          value={gen} onChange={
            (e)=> setGen(e.target.value)}>
            </input>


            <br></br>
            An aparitie:
            <br></br>
            <input id ="an" name = "an" type= "number"
          value={anAparitie} onChange={
            (e)=> setAn(e.target.value)}>

            </input>
            <h4></h4>
            Nume artist:
            <input id ="artist" name = "artist" type= "text"
          value={name} onChange={
            (e)=> setName(e.target.value)}>
            </input>
            <br></br>
            is Active?
            <input id ="active" name = "active" type= "text"
          value={isActive} onChange={
            (e)=> setActive(e.target.value)}>
            </input>
        </label>
        <input type ="submit" value = "Submit"></input>
      </form>
      </div>
    );

  }
export default AddForm