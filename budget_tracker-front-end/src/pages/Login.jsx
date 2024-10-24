import React, { useState } from 'react'
import { useAuth } from '../context/AuthContext'

export const Login = () => {
    const {login} = useAuth()
    const [credentials, setCredentials] = useState({username: '', password:''})

    const handleChange = (e) => {
        const {name, value} = e.target
        setCredentials({...credentials, [name]: value})
    }

    const handleSubmit = async(e) => {
        e.preventDefault()
        await (login(credentials))
    }
  return (
    <form onSubmit={handleSubmit}>
        <input type="text" name="username" placeholder='Username' value={credentials.username} onChange={handleChange} required />
        <input type="password" name="password" placeholder='Password' value={credentials.password} onChange={handleChange} required />
        <button type="submit">Login</button>
    </form>
  )
}
