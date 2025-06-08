import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import "../styles/Complaints.css";
import Footer from './Footer.js';
import Header from './Header.js';


function Complaints () {
    const [complaints, setComplaints] = useState([]);

    useEffect(() => {
       axios.get('http://127.0.0.1:8000/api/complaints/')
         .then(response => setComplaints(response.data))
         .catch(error => console.error(error));
     }, []);

     
     return (
          <div>
            <Header/>
            <main>
            <h1 className='client'>Клиент/Сервисная компания:</h1>
            <div className='info2'>
              <p>Информация о рекламациях Вашей техники</p>
            </div>
            <div className='tab'>
            <p className='result'>Таблица с данными (выдача результата)</p>
            <div className='info'>
              <form action="http://localhost:3000/machines"> 
                <button className='tab7'>Таблица: общая информация о машинах</button>
              </form>
              <form action="http://localhost:3000/maintenances">
                <button className='tab8'>Таблица: техническое обслуживание</button>
              </form>
              <button className='tab9'>Таблица: рекламации</button>
            </div>
            <table className='complaints'>
              <thead>
              <tr> 
                <th>Дата отказа</th>
                <th>Наработка</th>
                <th>Узел отказа</th>
                <th>Описание отказа</th>
                <th>Способ восстановления</th>
                <th>Используемые запасные части</th>
                <th>Дата восстановления</th>
                <th>Время простоя техники</th>
                <th>Машина</th>
                <th>Сервисная компания</th>
              </tr>
              </thead>
              <tbody>
              <tr> 
                <td>{complaints.map(complaint => (<p key={complaint.id}>{complaint.date_of_refusal}</p>))}</td>
                <td>{complaints.map(complaint => (<p key={complaint.id}>{complaint.development}</p>))}</td> 
                <td>{complaints.map(complaint => (<p key={complaint.id}>{complaint.failure_node}</p>))}</td>
                <td>{complaints.map(complaint => (<p key={complaint.id}>{complaint.description_of_failure}</p>))}</td>
                <td>{complaints.map(complaint => (<p key={complaint.id}>{complaint.recovery_method}</p>))}</td>
                <td>{complaints.map(complaint => (<p key={complaint.id}>{complaint.used_spare_parts}</p>))}</td>
                <td>{complaints.map(complaint => (<p key={complaint.id}>{complaint.date_of_restoration}</p>))}</td>
                <td>{complaints.map(complaint => (<p key={complaint.id}>{complaint.machine_downtime}</p>))}</td>
                <td>{complaints.map(complaint => (<p key={complaint.id}>{complaint.machine}</p>))}</td>
                <td>{complaints.map(complaint => (<p key={complaint.id}>{complaint.service_company}</p>))}</td>
              </tr>
              </tbody>
            </table>
            </div>
            </main>
            <Footer/>
          </div>
        );
      };

   export default Complaints;