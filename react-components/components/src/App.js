import React, { useState } from 'react';

import Datepicker from './components/Datepicker';
import BtnLoader from './components/btn-loader/BtnLoader';

function App() {
  const [date, setDate] = useState('02-10-2021');
  const [loading, setLoading] = useState(false);

  const toggleLoading = () => {
    setLoading(true);

    setTimeout(() => {
      setLoading(false);
    }, 3000);
  };

  return (
    <div className='App'>
      {/* <Datepicker label='Date of Birth' date={date} onDateChanged={setDate} /> */}
      {/* <div
        style={{
          fontSize: '1.5rem',
          height: '100vh',
        }}
      >
        <BtnLoader color='black' />
      </div> */}

      <button
        onClick={toggleLoading}
        style={{
          fontSize: '1rem',
          padding: '0.5em 0.8em',
          background: 'gray',
        }}
      >
        {loading ? <BtnLoader color='#fff' /> : 'Click to load'}
      </button>
    </div>
  );
}

export default App;
