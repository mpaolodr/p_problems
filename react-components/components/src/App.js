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
      <div
        className='testContainer'
        style={{
          outline: '2px solid blue',
          height: '20vh',
          width: '50%',
          margin: '0 auto',
          display: 'flex',
          alignItems: 'center',
          flexWrap: 'wrap',
        }}
      >
        <div
          className='box1'
          style={{
            flex: '0 0 20%',
            marginRight: 'auto',
            outline: '2px solid black',
          }}
        >
          box 1
        </div>

        <div
          className='box2'
          style={{
            display: 'none',
            flex: '0 0 75%',
            outline: '2px solid tomato',
          }}
        >
          box2
        </div>

        <div
          className='box3'
          style={{ flex: '0 0 75%', outline: '2px solid green' }}
        >
          box3
        </div>
      </div>
    </div>
  );
}

export default App;
