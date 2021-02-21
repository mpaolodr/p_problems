import React, { useState } from 'react';

import styled from 'styled-components';

import Datepicker from './components/Datepicker';
import BtnLoader from './components/btn-loader/BtnLoader';

import Test from './components/test';

const TextContainer = styled.div`
  border: 2px solid #cad1cf;
  width: 30%;
  border-radius: 21.5px;
  overflow: hidden;
  padding: 0;
  display: flex;
`;

const TextArea = styled.textarea`
  width: 100%;
  height: auto;
  padding: 0.4rem 0.8rem;
  background: #f1f1f1;
  border: none;
  resize: none;

  &:focus {
    outline: none;
  }
`;

function App() {
  const [date, setDate] = useState('02-10-2021');
  const [loading, setLoading] = useState(false);
  const [sHeight, setSHeight] = useState(null);

  const [text, setText] = useState('');

  console.log(text);

  const resize = (e) => {
    if (!sHeight) {
      setSHeight(e.target.scrollHeight);
    } else {
      if (sHeight !== e.target.scrollHeight) {
        e.target.attributes.rows.nodeValue =
          parseInt(e.target.attributes.rows.nodeValue) + 1;
        setSHeight(e.target.scrollHeight);
        console.log(e);
      }
    }
  };

  return (
    <div className='App'>
      <h2>App</h2>
    </div>
  );
}

export default App;
