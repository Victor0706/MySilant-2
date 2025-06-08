import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import "../styles/Maintenances.css";
import Footer from './Footer.js';
import Header from './Header.js';


function Maintenances () {
    const [maintenances, setMaintenances] = useState([]);

    useEffect(() => {
       axios.get('http://127.0.0.1:8000/api/maintenances/')
         .then(response => setMaintenances(response.data))
         .catch(error => console.error(error));
     }, []);

     return (
      <div>
        <Header/>
        <main>
        <h1 className='client'>Клиент/Сервисная компания:</h1>
        <div className='info2'>
          <p>Информация о проведенных ТО Вашей техники</p>
        </div>
        <div className='tab'>
        <p className='result'>Таблица с данными (выдача результата)</p>
        <div className='info'>
          <form action="http://localhost:3000/machines">
            <button className='tab4'>Таблица: общая информация о машинах</button> 
          </form>
          <button className='tab5'>Таблица: техническое обслуживание</button>
          <form action="http://localhost:3000/complaints">
            <button className='tab6'>Таблица: рекламации</button>
          </form>
        </div>
        <table className='maintenances'>
          <thead>
          <tr> 
            <th>Вид ТО</th>
            <th>Дата проведения ТО</th>
            <th>Наработка</th>
            <th>№ заказ-наряда</th>
            <th>Дата заказ-наряда</th>
            <th>Организация, проводившая ТО</th>
            <th>Зав. № машины</th>
            <th>Сервисная компания</th>
          </tr>
          </thead>
          <tbody>
          <tr> 
            <td>{maintenances.map(maintenance => (<p key={maintenance.id}>{maintenance.type_of_maintenance}</p>))}</td>
            <td>{maintenances.map(maintenance => (<p key={maintenance.id}>{maintenance.date_of_maintenance}</p>))}</td> 
            <td>{maintenances.map(maintenance => (<p key={maintenance.id}>{maintenance.development}</p>))}</td>
            <td>{maintenances.map(maintenance => (<p key={maintenance.id}>{maintenance.work_order_number}</p>))}</td>
            <td>{maintenances.map(maintenance => (<p key={maintenance.id}>{maintenance.work_order_date}</p>))}</td>
            <td>{maintenances.map(maintenance => (<p key={maintenance.id}>{maintenance.organization_maintenance}</p>))}</td>
            <td>{maintenances.map(maintenance => (<p key={maintenance.id}>{maintenance.machine}</p>))}</td>
            <td>{maintenances.map(maintenance => (<p key={maintenance.id}>{maintenance.service_company}</p>))}</td>
          </tr>
          </tbody>
        </table>
        </div>
        </main>
        <Footer/>
      </div>
    );
  };


   export default Maintenances;