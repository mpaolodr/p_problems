import React, { useState } from 'react';

import Datepicker from './components/Datepicker';
import BtnLoader from './components/btn-loader/BtnLoader';

function App() {
  const [date, setDate] = useState('02-10-2021');

  return (
    <div className='App'>
      {/* <Datepicker label='Date of Birth' date={date} onDateChanged={setDate} /> */}
      <div
        style={{
          fontSize: '1.5rem',
          height: '100vh',
        }}
      >
        <BtnLoader color='black' />
      </div>

      <button></button>
    </div>
  );
}

export default App;
