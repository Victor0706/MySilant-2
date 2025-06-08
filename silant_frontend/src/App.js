import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Machines from './components/Machines';
import Maintenances from './components/Maintenances';
import Complaints from './components/Complaints';
import Home from './components/Home'


function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/machines' element={<Machines/>} />
        <Route path='/maintenances' element={<Maintenances/>} />
        <Route path='/complaints' element={<Complaints/>} />
      </Routes>
    </Router>
  );
}


export default App;
