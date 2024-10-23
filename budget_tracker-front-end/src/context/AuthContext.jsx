import axios from "axios"
import React, { createContext, useContext, useEffect, useState } from "react"

const AuthContext = createContext()

export const AuthProvider = ({children}) => {
    const [user, setUser] = useState(null)
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        const  fetchUser = async () => {
            const token = localStorage.getItem('token')
            if(token){
                try{
                    const res = await axios.get('http://127.0.0.1:8000/api/user',{
                        headers:{Authorization: `Bearer ${token}`}
                    })
                    setUser(res.data)
                }catch(err){
                    console.error(err)
                }
            }
            setLoading(false)
        }
        fetchUser()
    }, [])

    const login = async(credentials) => {
        const res = await axios.post('https://127.0.0.1:8000/api/login', credentials)
        localStorage.setItem('token', res.data.token)
        setUser(res.data.user)
    }

    const logout = () => {
        localStorage.removeItem('token')
        setUser(null)
    }
    return(
        <AuthContext.Provider value={{user, loading, login, logout}}>
            {children}
        </AuthContext.Provider>
    )
}

export const useAuth =() => {
    return useContext(AuthContext)
}