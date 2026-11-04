import {useEffect, useState } from 'react'
import API from './services/api'

function App() {
  const [message, setMessage] = useState('Connecting to the backend...')

  useEffect(() => {
    const checkBackend = async () => {
      try {
        const response = await API.get('/health')
          setMessage(
            response.data.status === "healthy"?"Backend connected succeessfully!":"Backend is not healthy."
          )
      } catch (error) {
        console.error('Error connecting to the backend:', error)
        setMessage('Error connecting to the backend.')
      }
    }
    checkBackend()
  },[])
  return (
      <div>
        <h1>AI Resume Intelligence</h1>
        <p>{message}</p>
      </div>
  )
}

export default App
