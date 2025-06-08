import React from 'react';
import '../styles/Header.css';
import Logotype_accent_RGB_1 from '../image/Logotype_accent_RGB_1.jpg'


function Header () {
    return (
        <div className='header'>
            <div className='header2'> 
              <img className='img' src={Logotype_accent_RGB_1}></img>  
              <p className='telephone'>+7-8352-20-12-09, telegram - https://t.me</p>
              <button className='btn'>авторизация</button>
            </div>
            <div className='book'>
              <p className='book1'>Электронная сервисная книжка "Мой Силант"</p>
            </div>
        </div>
    )

}

export default Header