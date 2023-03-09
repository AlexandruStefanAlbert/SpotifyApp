import React from "react"

const ArtistList= ({artist})=>(
    <ul>
    {
    artist && artist.length>0 && artist.map((userObj, index) =>(
        <li key = {userObj}>{userObj.name} </li>
    ))
    }

    </ul>
);
export default ArtistList