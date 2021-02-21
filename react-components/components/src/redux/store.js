import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers';

let userState;
const userFromLocalStorage = localStorage.getItem('user');

if (userFromLocalStorage) {
  userState = {
    user: JSON.parse(userFromLocalStorage),
  };
}

const store = createStore(rootReducer, userState, applyMiddleware(thunk));

export default store;
