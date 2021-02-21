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
  return (
    <div className='App'>
      <h2>Test</h2>
    </div>
  );
}

export default App;

// MEMOIZED Selectors are selectors that save the most recent result value and if you call them multiple times
// with the same inputs, it wil return the same result value
// if you call them with DIFFERENT INPUTS, they will recalculate a new result value and cache it and return the new result

// The Reselect library provides a createSelector API that will generate memoized selector functions.
// createSelector accepts one or more "input selector" functions as arguments, plus an "output selector",
// and returns the new selector function. Every time you call the selector:

// STUDY MEMOIZED SELECTORS
