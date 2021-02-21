// const initState = {
//   user: {},
// };

// export default function userReducer(state = initState, action) {
//   switch (action.type) {
//     default:
//       return state;
//   }
// }

import {
  createSlice,
  createAsyncThunk,
  createEntityAdapter,
} from '@reduxjs/toolkit';

// we can only pass a single argument to thunk, if we want to pass multiple stuff, we need to pass it in an object
// export const editUser = createAsyncThunk(
//   'user/editUser',
//   async ({ id, newName, newProperty }) => {
//     // await axios.patch("/fakeDB/${id}", {name: newName, property: newProperty});
//     // const updatedUser = await axios.get("/fakeDB/${id}")
//     // return updatedUser
//   }
// );

const userAdapter = createEntityAdapter();

const initState = userAdapter.getInitialState({
  users: {},
  status: 'idle',
});

const userSlice = createSlice({
  name: 'user',
  initialState: initState,
  reducers: {
    changeUserId(state, action) {
      state.userInfo.id = action.payload;
    },
    // when addUser action is called, prepare() gets called first
    addUser: {
      reducer(state, action) {
        const { id, name } = action.payload;

        state.newUser = { id, name };
      },

      prepare(id, name) {
        return {
          payload: {
            id,
            name,
          },
        };
      },
    },

    // addTest: userAdapter.addOne({ id: 2, name: 'TEST ADAPTER' }),
  },
  // extraReducers: (builder) => {
  //   builder
  //     .addCase(editUser.pending, (state, action) => {
  //       state.status = 'loading';
  //     })
  //     .addCase(editUser.fulfilled, (state, action) => {
  //       state.users = action.payload;
  //       state.status = 'idle';
  //     });
  // },
});

export const { changeUserId, addUser, addTest } = userSlice.actions;
export default userSlice.reducer;
