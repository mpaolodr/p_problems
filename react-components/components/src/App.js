import React, { useState } from 'react';
import { Route, Switch, Link } from 'react-router-dom';

import styled from 'styled-components';

import Datepicker from './components/Datepicker';
import BtnLoader from './components/btn-loader/BtnLoader';
import ReactDp from './components/ReactDP';
import Grid from './components/Grid';
import Carousel from './components/carousel/Carousel';
import AnotherOne from './components/another-carousel/AnotherOne';
import Page from './components/route-test/Page';
import Home from './components/route-test/Home';

import AnimatedSwitch from './components/AnimatedSwitch';

function App() {
  const photos = [
    'https://res.cloudinary.com/mpaolodr/image/upload/v1606105334/sample.jpg',
    'https://res.cloudinary.com/mpaolodr/image/upload/v1600361221/ne4xxl26ltcuagldepao.jpg',
    'https://res.cloudinary.com/mpaolodr/image/upload/v1582594359/samples/bike.jpg',
    'https://res.cloudinary.com/mpaolodr/image/upload/v1582594357/samples/sheep.jpg',
  ];

  return (
    <div className='App'>
      <nav>
        <Link to='/'>Home</Link>
        <Link to='/page'>Page</Link>
      </nav>

      {/* <Switch>
        <Route path='/page' className={`fade fade-${state}`} component={Page} />

        <Route path='/' component={Home} />
      </Switch> */}

      <AnimatedSwitch />
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
