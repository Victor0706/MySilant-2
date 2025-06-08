import React, { useState, useEffect } from "react";
import axios from 'axios';  
import { useParams, Link } from 'react-router-dom';
  

function User () {  
    const [user, setUser] = useState([]);
       
    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/users/')
          .then(response => setUser(response.data))
          .catch(error => console.error(error));
      }, []);


        return (  
            <div>  
                {user.map(user => (<p key={user.id}>{user.username}</p>))}
            </div>  
        );  



}
    
export default User;
