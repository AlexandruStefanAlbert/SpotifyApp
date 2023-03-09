import React, {useContext, useState} from "react";
import swal from "sweetalert";
import AuthContext from "./authProvider";
import axios from "axios";
import { json } from "react-router-dom";
async function loginUser(credentials){


    return fetch("http://localhost:8086/token",
    {
        mode : 'no-cors',
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'accept': 'application/json'
        },
        body: new URLSearchParams(credentials)
    }).then(credentials =>credentials.json);
}

function LoginForm(){
    const [username, setUsername]= useState('');
    const [password, setPassword]= useState('');
    const {setAuth} = useContext(AuthContext);
    
        const handleSubmit = async e =>{
        e.preventDefault();
        const response = await loginUser({
            username,
            password
        });           
    
        let cookie = document.cookie;
        

        if(cookie) // ???????????
        {
            swal("Succes", "succes",
            {
                buttons: false,
                timer: 2000
            }).then((value)=>{
                localStorage.setItem("access_token", response["access_token"]);
                localStorage.setItem('user', JSON.stringify(response['user']));
                window.location.href="/Spotify";
            } );
        }
        else{
            swal("Failed", "Username or password wrong");
           
        }
        //Send a POST request to the login route with the username and apss
        
    }
    return(
        <div id ="login-form">
        <form onSubmit={handleSubmit}>
            <label>
                Username:
                <input htmlFor = "username" id="username" name="username" type = "text" value={username} onChange={
                    (e)=>setUsername(e.target.value)}></input>
            </label>
            <label>
                Password:
                <input htmlFor = "password" id="password" name="password"type="password" value={password} onChange={
                    (e) => setPassword(e.target.value)}></input>
            </label>
            <input type="submit" value="Login"></input>
        </form>
        </div>
    );
}
export default LoginForm