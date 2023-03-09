import React from "react"
const SongList = ({song})=>(
    <ul>
    {
    song && song.length>0 && song.map((userObj, index) =>(
        <li key = {userObj}>{userObj.title} {userObj.anAparitie}</li>
    ))
    }

    </ul>
);

export default SongList