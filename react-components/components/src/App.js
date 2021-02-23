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

const obj = {
  success: false,
  error: {
    message: 'invalid input syntax for type integer: ""',
    length: 101,
    name: 'QueryFailedError',
    severity: 'ERROR',
    code: '22P02',
    file: 'numutils.c',
    line: '259',
    routine: 'pg_strtoint32',
    query:
      'UPDATE "users" SET "genderId" = $2, "date_of_birth" = $3, "first_name" = $4, "last_name" = $5, "city" = $6, "region" = $7, "country" = $8, "account_image_url" = $9, "updatedAt" = CURRENT_TIMESTAMP WHERE "id" IN ($1)',
    parameters: [
      '1',
      '',
      '1992-02-05T00:00:00.000Z',
      'Marlon',
      'Del Rosario',
      'Springvale',
      '',
      'USA',
      'https://account-microservice.s3.ca-central-1.amazonaws.com/ab9dae0d-5b1a-4de4-9d79-141595548819-coffee.jpg',
    ],
  },
};

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
