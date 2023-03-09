import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Spotify from './component/spotifyPage';
import LoginForm from './component/loginPage';
import AddForm from './component/addSongArtist';
const router = createBrowserRouter(
  [
    {
      path: "/",
      element: <LoginForm></LoginForm>
    },
    {
      path:"/Spotify",
      element: <Spotify></Spotify>
    },
    {
      path: "/AddSong",
      element: <AddForm></AddForm>
    }
  ]
);


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <RouterProvider router={router}/>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
