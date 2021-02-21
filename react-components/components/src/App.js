import React, { useState } from 'react';
import store from './redux/store';
import { useSelector } from 'react-redux';

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
  store.dispatch({ type: 'todos/todosAdded', payload: 'Added Enchancer' });
  return (
    <div className='App'>
      <h2>App</h2>
    </div>
  );
}

export default App;
