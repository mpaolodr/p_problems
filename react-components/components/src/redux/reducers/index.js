// without combineReducer from Redux core library
// import todosReducer from './todoSlice';
// import filtersReducer from './filtersSlice';

// export default function rootReducer(state = {}, action) {
//   return {
//     todos: todosReducer(state.todos, {}),
//     filters: filtersReducer(state.filters, action),
//   };
// }

import { combineReducers } from 'redux';
import todosReducer from './todoSlice';
import filtersReducer from './filtersSlice';

const rootReducer = combineReducers({
  todos: todosReducer,
  filters: filtersReducer,
});

export default rootReducer;
