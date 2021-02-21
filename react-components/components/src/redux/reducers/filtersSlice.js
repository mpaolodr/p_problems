// const initState = {
//   status: 'ALL',
//   colors: [],
// };

// const filtersReducer = (state = initState, action) => {
//   switch (action.type) {
//     case 'filters/statusFilterChanged':
//       return {
//         ...state,
//         status: action.payload,
//       };
//     default:
//       return state;
//   }
// };

// export default filtersReducer;

import { createSlice } from '@reduxjs/toolkit';

const initState = {
  status: 'ALL',
  colors: [],
};

const filtersSlice = createSlice({
  name: 'filter',
  initialState: initState,
  reducers: {
    statusFilterChanged(state, action) {
      state.status = action.payload;
    },
  },
});

export const { statusFilterChanged } = filtersSlice.actions;
export default filtersSlice.reducer;
