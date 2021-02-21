import React, { useState } from 'react';
import store from './redux/store';
import { useSelector, useDispatch, shallowEqual } from 'react-redux';
import { selectTodoIds } from './redux/reducers/todoSlice';
import { changeUserId, addUser } from './redux/reducers/userSlice';
import { todosAdded } from './redux/reducers/todoSlice';

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
  // const selectTodoIds = (state) => state.todos.map((todo) => todo.id);

  // const getIds = useSelector(selectTodoIds);
  const dispatch = useDispatch();

  // dispatch({ type: 'todos/todosAdded', payload: 'Test Something' });

  console.log('STATE: ', store.getState());

  // const todos = useSelector((state) => state.todos);

  // console.log(todos);

  dispatch(changeUserId(2));

  console.log('AFTER DISPATCH: ', store.getState());

  dispatch(addUser(3, 'TABBY TOOLKIT'));
  console.log('AFTER DISPATCH: ', store.getState());

  // const renderedListItems = getIds.map((todoId) => {
  //   return (
  //     <h2 key={todoId} id={todoId}>
  //       TODO
  //     </h2>
  //   );
  // });

  return (
    <div className='App'>
      {/* {renderedListItems} */}
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
