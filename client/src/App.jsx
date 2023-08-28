import './App.css';
import { SignupForm } from './components/Signup';
import {createBrowserRouter, Route, createRoutesFromElements, RouterProvider} from 'react-router-dom';
import React, {useEffect, useState} from 'react';
import Community from './components/Community.jsx';
import Home from './components/Home.jsx';
import Personal from './components/Personal.jsx';
import Login from './components/Login.jsx';



function App() {

  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route
      path="/home"
      element={<Home />}
      />
      
  )
  )
  return (
    <div >
      <RouterProvider router={router}/>
    </div>
    
  );
}

export default App;