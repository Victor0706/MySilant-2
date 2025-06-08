import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import "../styles/Machines.css";
import Footer from './Footer.js';
import Header from './Header.js';
import User from './User.js'


function Machines () {
    const [machines, setMachines] = useState([]);


    useEffect(() => {
       axios.get('http://127.0.0.1:8000/api/machines/')
         .then(response => setMachines(response.data))
         .catch(error => console.error(error));
     }, []);



     return (
       <div>
         <Header/>
         <main>
         <h1 className='client'>Клиент/Сервисная компания: <User/></h1>
         <div className='info2'>
           <p>Информация о комплектации и технических</p>
           <p>характеристиках Вашей техники</p>
         </div>
         <div className='tab'>
         <p className='result'>Таблица с данными (выдача результата)</p>
         <div className='info'>
           <button className='tab1'>Таблица: общая информация о машинах</button> 
           <form action="http://localhost:3000/maintenances">
             <button className='tab2'>Таблица: техническое обслуживание</button>
           </form>
           <form action="http://localhost:3000/complaints">
             <button className='tab3'>Таблица: рекламации</button>
           </form>
         </div>
         <table className='machines'>
           <thead>
           <tr> 
             <th>Зав. № машины</th>
             <th>Модель техники</th>
             <th>Модель двигателя</th>
             <th>Зав. № двигателя</th>
             <th>Модель трансмиссии</th>
             <th>Зав. № трансмиссии</th>
             <th>Модель ведущего моста</th>
             <th>Зав. № ведущего моста</th>
             <th>Модель управляемого моста</th>
             <th>Зав. № управляемого моста</th>
             <th>Договор поставки №</th>
             <th>Дата отгрузки с завода</th>
             <th>Грузополучатель (конечный потребитель)</th>
             <th>Адрес поставки (эксплуатации)</th>
             <th>Комплектация (доп. опции)</th>
             <th>Клиент</th>
             <th>Сервисная компания</th>
           </tr>
           </thead>
           <tbody>
           <tr> 
             <td>{machines.map(machine => (<p key={machine.id}>{machine.machine_number}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.model_of_equipment}</p>))}</td> 
             <td>{machines.map(machine => (<p key={machine.id}>{machine.engine_model}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.engine_number}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.transmission_model}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.transmission_number}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.model_of_driving_axle}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.drive_axle_number}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.model_of_controlled_bridge}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.controlled_bridge_number}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.supply_contract_number}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.shipment_date}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.consignee}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.delivery_address}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.equipment}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.client}</p>))}</td>
             <td>{machines.map(machine => (<p key={machine.id}>{machine.service_company}</p>))}</td>
           </tr>
           </tbody>
         </table>
         </div>
         </main>
         <Footer/>
       </div>
     );
   };

   export default Machines;