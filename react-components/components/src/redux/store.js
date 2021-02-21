// before reduxjs toolkit
// import { createStore, applyMiddleware } from 'redux';
// import thunk from 'redux-thunk';
// import { composeWithDevTools } from 'redux-devtools-extension';
// import rootReducer from './reducers';

// let userState;
// const userFromLocalStorage = localStorage.getItem('user');

// if (userFromLocalStorage) {
//   userState = {
//     user: JSON.parse(userFromLocalStorage),
//   };
// }

// const composedEnhancer = composeWithDevTools(applyMiddleware(thunk));

// const store = createStore(rootReducer, userState, composedEnhancer);

// export default store;

import { configureStore } from '@reduxjs/toolkit';

import todosReducer from './reducers/todoSlice';
import filtersReducer from './reducers/filtersSlice';
import userReducer from './reducers/userSlice';

let userState;
const userFromLocalStorage = localStorage.getItem('user');

if (userFromLocalStorage) {
  userState = {
    userInfo: JSON.parse(userFromLocalStorage),
  };
}

const store = configureStore({
  reducer: {
    todos: todosReducer,
    filters: filtersReducer,
    user: userReducer,
  },

  preloadedState: { user: userState },
});

export default store;

// having multiple selectors is a good idea, each selector dealing with one slice
