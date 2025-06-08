import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import "../styles/Home.css";
import Footer from './Footer.js';
import Header from './Header.js';



function Home () {
    const [machines, setMachines] = useState([]);

    useEffect(() => {
       axios.get('http://127.0.0.1:8000/api/machines/')
         .then(response => setMachines(response.data))
         .catch(error => console.error(error));
     }, []);

     return (
       <div>
         <Header/>
         <main className='info3'>
         <div className='info4'>
           <p>Проверьте комплектацию и технические характеристики</p>
           <p>техники Силант</p>
         </div>
         <form className='form' action="http://localhost:3000/machines">
           <input className="input" type="text" placeholder="Заводской номер:" required></input>
           <input className="input" type="submit" value="Поиск"></input>
         </form>
         <div className='info2'>
           <p>Информация о комплектации и технических</p>
           <p>характеристиках Вашей техники</p>
         </div>
         <div className='tab'>
         <p className='result'>Таблица с данными (выдача результата)</p>
         <table className='home'>
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
           </tr>
           </tbody>
         </table>
         </div>
         </main>
         <Footer/>
       </div>
     );
   };

   export default Home;