import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension';
import rootReducer from './reducers';

let userState;
const userFromLocalStorage = localStorage.getItem('user');

if (userFromLocalStorage) {
  userState = {
    user: JSON.parse(userFromLocalStorage),
  };
}

const testMiddleWare = () => (next) => (action) => {
  console.log('TESTING!');

  return next(action);
};

const composedEnhancer = composeWithDevTools(applyMiddleware(testMiddleWare));

const store = createStore(rootReducer, userState, composedEnhancer);

export default store;
