// const initState = {
//   todos: [
//     { id: 0, text: 'Learn React', completed: true },
//     { id: 1, text: 'Learn Redux', completed: false, color: 'purple' },
//     { id: 2, text: 'Build something fun!', completed: false, color: 'blue' },
//   ],
//   filters: {
//     status: 'ALL',
//     colors: [],
//   },
// };

// before toolkit
// import { createSelector } from 'reselect';

// export const selectTodoIds = createSelector(
//   (state) => state.todos,
//   (todos) => todos.map((todo) => todo.id)
// );

// const initState = [
//   { id: 0, text: 'Learn React', completed: true },
//   { id: 1, text: 'Learn Redux', completed: false, color: 'purple' },
//   { id: 2, text: 'Build something fun!', completed: false, color: 'blue' },
// ];

// // AUTO INCREMENTING ID
// function nextTodoId(todos) {
//   const maxId = todos.reduce((maxId, todo) => Math.max(todo.id, maxId), -1);
//   return maxId + 1;
// }

// export const todosReducer = (state = initState, action) => {
//   switch (action.type) {
//     case 'todos/todosAdded':
//       return [
//         ...state,
//         {
//           id: nextTodoId(state),
//           text: action.payload,
//           completed: false,
//         },
//       ];

//     case 'todos/todoToggled':
//       return state.todos.map((todo) => {
//         if (todo.id !== action.payload) {
//           return todo;
//         }

//         return {
//           ...todo,
//           completed: !todo.completed,
//         };
//       });

//     default:
//       return state;
//   }
// };

// export default todosReducer;

import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

const initState = [];

const todoSlice = createSlice({
  name: 'todos',
  initialState: initState,
  reducers: {
    todosAdded(state, action) {
      // this mutating code is okay inside slice?!!
      state.push(action.payload);
    },
    todosToggled(state, action) {
      const todo = state.find((todo) => todo.id === action.payload);
      todo.completed = !todo.completed;
    },
    todosLoading(state, action) {
      return {
        ...state,
        status: 'loading',
      };
    },
  },
});

export const fetchTodos = createAsyncThunk('todos/fetchTodos');

export const { todosAdded, todosToggled, todosLoading } = todoSlice.actions;
export default todoSlice.reducer;
