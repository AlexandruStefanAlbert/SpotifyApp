import React from "react"

const CollectionList= ({collection})=>(
    <ul>
    {
    collection && collection.length>0 && collection.map((userObj, index) =>(
        <li key = {userObj}>{userObj} </li>
    ))
    }

    </ul>
);
export default CollectionList