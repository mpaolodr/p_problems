import React, { useState } from 'react';

import Datepicker from './components/Datepicker';

function App() {
  const [date, setDate] = useState('02-10-2021');

  console.log(date, 'FROM APP');
  return (
    <div className='App'>
      <Datepicker label='Date of Birth' date={date} onDateChanged={setDate} />
    </div>
  );
}

export default App;
