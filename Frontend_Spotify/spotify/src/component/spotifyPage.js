import SongList from './songList';
import './App.css';
import { useState, useEffect } from 'react';
import ArtistList from './artistList';
import CollectionList from './collectionList';
import AddForm from './addSongArtist';

function Spotify() {
  const [song, setSong] = useState([]);
  const [artist, setArtist]= useState([]);
  const [collection, setCollection]= useState([]);
  

  const fetchData1 = () => {
    return fetch("http://localhost:8086/songs")
            .then((response)=> response.json())
            .then((data) => setSong(data));
  }
  const fetchData2 = () => {
    return fetch("http://localhost:8086/artists")
            .then((response)=> response.json())
            .then((data) => setArtist(data));
  }

  const fetchData3 = () => {
    return fetch("http://localhost:8086/collections/6/song")
            .then((response)=> response.json())
            .then((data) => setCollection(data));
  }

  

  
useEffect(()=>{
  fetchData1()
}, [])

useEffect(()=>{
  fetchData2()
}, [])

useEffect(()=>{
  fetchData3()
}, [])


return( 
  
 <div className="App">
    <header className ="App-header">
      <a href='/addSong'>Add new Song and Artist</a>
      <div>
        <h1>Artists</h1>
        <ArtistList artist={artist}></ArtistList>
      </div>
      <div>
        <h1>Songs list:</h1>
          <SongList song={song} />
      </div>
      <div>
        <h1>Iron Maiden collections</h1>
        <CollectionList collection={collection}></CollectionList>
      </div>
    </header>
  </div>
  
);
}
export default Spotify;
