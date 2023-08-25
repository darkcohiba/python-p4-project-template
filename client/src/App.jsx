
import { useEffect } from 'react'
import './App.css'
import Login from './components/login'
import Signup from './components/signup'
import useSWR from 'swr';


function App() {

  const fetcher = (url) => fetch(url).then((res) => res.json());
  
  const { data, error } = useSWR("/api/check_session", fetcher);

  if (error) {
    return <div>Failed to load session</div>;
  }
  if (!data) {
    return <div>Loading...</div>;
  }
  
  const handleLogout = function() {
    fetch('/api/logout', {
      method: 'DELETE', 
    })
  }
  
  return (
    <>
      <div>Session Data: {JSON.stringify(data)}</div>
      <Login />
      <Signup />
      <button onClick={handleLogout}>Logout</button>
    </>
  )
}

export default App
