## Rules of thumb when deciding what kind of data should be in redux store

Do other parts of the application care about this data?
Do you need to be able to create further derived data based on this original data?
Is the same data being used to drive multiple components?
Is there value to you in being able to restore this state to a given point in time (ie, time travel debugging)?
Do you want to cache the data (ie, use what's in state if it's already there instead of re-requesting it)?
Do you want to keep this data consistent while hot-reloading UI components (which may lose their internal state when swapped)?

_notes_

1. we can call _useSelector_ multiple times in a single component!

- each call to useSelector should return the _smalles amount of state_ possible

2. everytime we use _map_ or _filter_ or any array methods that return new arrays, we're basically creating
   new reference of the state so _useSelector_ will force the component to re-render including the child components after every _dispatched action_

```To avoid re-rendering needlesly

2 OPTIONS:
1. Using SHALLOWEQUAL as an argument to useSelector
2. Memoized Selectors

```

3. _Memoization_ is a kind of caching, saving the results of an expensive calculation and reusing those results if we see the same inputs later

4. _Memoized Selector Functions_ are selectors that save the most recent result value and if you call them multiple times with _the same inputs_, will return the same result value. If you call them with different inputs than last time, they will recalculate a new result value, cache it, and return the new result

5. _Reselect_ library provides _createSelector API_ that will generat memoized selector functions

- _createSelector_ accepts one or more _input selector_ functions as arguments plus an _output selector_ and returns the new selector function

```
EVERY TIME WE CALL THE SELECTOR:

- All "input selectors" are called with all of the arguments
- If any of the input selector return values have changed, the "output selector" will re-run
- All of the input selector results become arguments to the output selector
- The final result of the output selector is cached for next time


```

6. _Memoized selectors are only helpful_ when you actually derive additional values from the original data. If you are only looking up and returning an existing value, you can keep the selector as a plain function.

7. The term _entities_ is a term that means _unique items with ID_

8. instead of using _loading_ as a boolean value, which limits us to 2 possibilities (true or false), in reality, _it's possible for a request to actually be in many different states_

```possible loading states

1. hasn't started at all
2. in progress
3. succeeded
4. failed
5. succeeded but now back in a situation where we might want to refresh

- because of this, it's better to STORE LOADING STATE AS A STRING ENUM VALUE


```

9. _FSA or Flux Standard Actions_ are suggested approach for how to organize fields inside of action objects

```FSA

ACTIONS:

1. If your action object has any actual data, that "data" value of your action should always go in action.payload
2. An action may also have an action.meta field with extra descriptive data
3. An action may have an action.error field with error information

SO ALL REDUX ACTIONS MUST:

1. be a plain JavaScript object
2. have a type field

IF YOU WRITE YOUR ACTIONS USING FSA PATTERN:

1. have a payload field
2. have an error field
3. have a meta field



```

10. In larger redux apps, it is common to store data in _normalized state structure_

```What does Normalization mean?

1. Making sure there is only one copy of each piece of data
2. Storing items in a way that allows directly finding items by ID
3. Referring to other items based on IDs, instead of copying the entire item


- this means we normally organize our data as objects instead of arrays
- where the ITEM ID are the keys, and the items themselves are the values


1. Normalization is commonly used in Redux apps
2. The primary benefits are being able to look up individual items by ID and ensure that only one copy of an item exists in the state
```

## Redux Toolkit

1. Setting up the store

```Setting up the root reducer and store without toolkit

reducer.js

import todosReducer from './features/todos/todosSlice'
import filtersReducer from './features/filters/filtersSlice'
import { combineReducers } from 'redux'

const rootReducer = combineReducers({
  todos: todosReducer,
  filters: filtersReducer,
})

export default rootReducer


store.js

import { createStore, applyMiddleware } from 'redux'
import { composeWithDevTools } from 'redux-devtools-extension'
import thunk from 'redux-thunk'
import rootReducer from './reducer'

const composedEnhancer = composeWithDevTools(applyMiddleware(thunk))

const store = createStore(rootReducer, composedEnhancer)

export default store



Notice that the setup process takes several steps. We have to:

1. Combine the slice reducers together to form the root reducer
2. Import the root reducer into the store file
3. Import the thunk middleware, applyMiddleware, and composeWithDevTools APIs
4. Create a store enhancer with the middleware and devtools
5. Create the store with the root reducer

```

```using configureStore to create store and combinReducers

configureStore API simplifies the store setup process
- it wraps around the Redux core creatStore API and handles most of the store setup for us automatically
- those 5 steps we needed to ocmbine reducers and setup store can now take one step only


import { configureStore } from '@reduxjs/toolkit'
import todosReducer from './features/todos/todosSlice'
import filtersReducer from './features/filters/filtersSlice'

const store = configureStore({
  reducer: {
    todos: todosReducer,
    filters: filtersReducer,
  },
})

export default store

That one call to configureStore did:
1. It combined todosReducer and filtersReducer into the root reducer function, which will handle a root state that looks like {todos, filters}
2. It created a Redux store using that root reducer
3. It automatically added the thunk middleware
4. It automatically added more middleware to check for common mistakes like accidentally mutating the state
5. It automatically set up the Redux DevTools Extension connection
```

2. Writing Slices

```
createSlice API helps us simplify our redux reducer logic and actions

createSlice does severla important thing for us:

1. We can write the case reducers as functions inside of an object, instead of having to write a switch/case statement
2. The reducers will be able to write shorter immutable update logic
3. All the action creators will be generated automatically based on the reducer functions we've provided

Using createSlice

createSlice takes an object with three main options fields:

1. name: a string that will be used as the prefix for generated action types
2. initialState: the initial state of the reducer
3. reducers: an object where the keys are strings, and the values are "case reducer" functions that will handle specific actions


EXAMPLE:

import { createSlice } from '@reduxjs/toolkit'

const initialState = []

const todosSlice = createSlice({
  name: 'todos',
  initialState,
  reducers: {
    todoAdded(state, action) {
      state.push(action.payload)
    },
    todoToggled(state, action) {
      const todo = state.find(todo => todo.id === action.payload)
      todo.completed = !todo.completed
    },
    todosLoading(state, action) {
      return {
        ...state,
        status: 'loading'
      }
    }
  }
})

export const { todoAdded, todoToggled, todosLoading } = todosSlice.actions

export default todosSlice.reducer


IN THE EXAMPLE ABOVE:

1. We write case reducer functions inside the reducers object, and give them readable names
2. createSlice will automatically generate action creators that correspond to each case reducer function we provide
- the generated action creators will be available as slice.actions.todoAdded
- we typically destructure and export those like how we do in the old code

3. createSlice automatically returns the existing state in the default case.
4. createSlice allows us to safely "mutate" our state!
5. But, we can also make immutable copies like before if we want to

- the complete reducer function is available as slice.reducer and we typically export default slice.reducer

```

```

Redux Toolkit's createSlice function lets you write immutable updates an easier way!

FROM THIS:

function handwrittenReducer(state, action) {
  return {
    ...state,
    first: {
      ...state.first,
      second: {
        ...state.first.second,
        [action.someId]: {
          ...state.first.second[action.someId],
          fourth: action.someValue
        }
      }
    }
  }
}

With immer:

function reducerWithImmer(state, action) {
  state.first.second[action.someId].fourth = action.someValue
}


NOTE!!

You can only write "mutating" logic in Redux Toolkit's createSlice and createReducer because they use Immer inside! If you write mutating logic in reducers without Immer, it will mutate the state and cause bugs!

```

```refactoring todoSlice

export default function todosReducer(state = initialState, action) {
  switch (action.type) {
    case 'todos/todoAdded': {
      const todo = action.payload
      return {
        ...state,
        entities: {
          ...state.entities,
          [todo.id]: todo,
        },
        status: 'idle',
      }
    }
    case 'todos/todoToggled': {
      const todoId = action.payload
      const todo = state.entities[todoId]

      return {
        ...state,
        entities: {
          ...state.entities,
          [todoId]: {
            ...todo,
            completed: !todo.completed,
          },
        },
      }
    }
    case 'todos/colorSelected': {
      const { color, todoId } = action.payload
      const todo = state.entities[todoId]
      return {
        ...state,
        entities: {
          ...state.entities,
          [todoId]: {
            ...todo,
            color,
          },
        },
      }
    }
    case 'todos/todoDeleted': {
      const newEntities = { ...state.entities }
      delete newEntities[action.payload]

      return {
        ...state,
        entities: newEntities,
      }
    }
    case 'todos/allCompleted': {
      const newEntities = { ...newEntities }

      Object.values(newEntities).forEach((todo) => {
        newEntities[todo.id] = {
          ...todo,
          completed: true,
        }
      })
    }
    case 'todos/completedCleared': {
      const newEntities = { ...newEntities }

      Object.values(newEntities).forEach((todo) => {
        if (todo.completed) {
          delete newEntities[todo.id]
        }
      })

      return {
        ...state,
        entities: newEntities,
      }
    }
    case 'todos/todosLoaded': {
      const newEntities = {}

      action.payload.forEach((todo) => {
        newEntities[todo.id] = todo
      })

      return {
        ...state,
        entities: newEntities,
        status: 'idle',
      }
    }

    case 'todos/todosLoading': {
      return {
        ...state,
        status: 'loading',
      }
    }
    default:
      return state
  }
}


AFTER TOOLKIT:

const todoSlice = {
  name: 'todos',
  initialState,
  reducers: {
    todoAdded(state, action) {
      const todo = action.payload
      state.entities[todo.id] = todo
    },
    todoToggled(state, action) {
      const todoId = action.payload
      const todo = state.entities[todoId]

      todo.completed = !todo.completed
    },
    colorSelected: {
      reducer(state, action) {
        const { color, todoId } = action.payload
        state.entities[todoId].color = color
      },
      prepare(todoId, color) {
        return {
          payload: { todoId, color },
        }
      },
    },
    todoDeleted(state, action) {
      delete state.entities[action.payload]
    },
    allCompleted(state, action) {
      Object.values(state.entities).forEach((todo) => {
        todo.completed = true
      })
    },
    completedCleared(state, action) {
      Object.values(state.entities).forEach((todo) => {
        if (todo.completed) {
          delete state.entities[todo.id]
        }
      })
    },
    todosLoaded(state, action) {
      const newEntities = {}

      action.payload.forEach((todo) => {
        newEntities[todo.id] = todo
      })

      state.entities = newEntities
      state.status = 'idle'
    },

    todosLoading(state, action) {
      state.status = 'loading'
    },
  },
}

export const {
  todoAdded,
  todoToggled,
  colorSelected,
  todoDeleted,
  allCompleted,
  completedCleared,
  todosLoaded,
  todosLoading,
} = todoSlice.actions
export default todoSlice.reducer


NOTES:

1. The action creators for todoAdded and todoToggled only need to take a single parameter, like an entire todo object or a todo ID. But, what if we need to pass in multiple parameters, or do some of that "preparation" logic we talked about like generating a unique ID?

createSlice lets us handle those situations by adding a "prepare callback" to the reducer. We can pass an object that has functions named reducer and prepare. When we call the generated action creator, the prepare function will be called with whatever parameters were passed in. It should then create and return an object that has a payload field (or, optionally, meta and error fields), matching the Flux Standard Action convention.

```

3. Writing Thunks

```createAsyncThunk

BEFORE CREATEASYNCTHUNK

export const fetchTodos = () => async (dispatch) => {
  dispatch(todosLoading())
  const response = await client.get('/fakeApi/todos')
  dispatch(todosLoaded(response.todos))
}

AFTER:

export const fetchTodos = createAsyncThunk('todos/fetchTodos', async () => {
  const response = await client.get('/fakeApi/todos')
  return response.todos
})


BEFORE CREATEASYNCTHUNK:

export function saveNewTodo(text) {
  return async function saveNewTodoThunk(dispatch, getState) {
    const initialTodo = { text }
    const response = await client.post('/fakeApi/todos', { todo: initialTodo })
    dispatch(todoAdded(response.todo))
  }
}

AFTER:

export const saveNewTodo = createAsyncThunk(
  'todos/saveNewTodo',
  async (text) => {
    const initialTodo = { text }
    const response = await client.post('/fakeApi/todos', initialTodo)
    return response.todo
  }
)



- createAsyncThunk will generate three action creators and action types, plus a thunk function
that automatically dispatches those actions when called. In this case, the action creators and
their types are:

1. fetchTodos.pending: todos/fetchTodos/pending
2. fetchTodos.fulfilled: todos/fetchTodos/fulfilled
3. fetchTodos.rejected: todos/fetchTodos/rejected

- createSlice also accepts an extraReducers option, where we can have the same slice reducer listen for other action types
- This field should be a callback function with a builder parameter, and we can call builder.addCase(actionCreator, caseReducer) to listen for other actions.

NOTES ON THUNKS:
- You can only pass one argument to the thunk when you dispatch it. If you need to pass multiple values, pass them in a single object
- The payload creator will receive an object as its second argument, which contains {getState, dispatch}, and some other useful values
- The thunk dispatches the pending action before running your payload creator, then dispatches either fulfilled or rejected based on whether the Promise you return succeeds or fails
```

4. Normalizing State

```createEntityAdapter

Redux Toolkit includes a createEntityAdapter API that has prebuilt reducers for typical data update operations with normalized state.

- this includes:

1. Adding items from a slice
2. Updating items from a slice
3. Removing items from a slice

- also generates some memoized selectors for reading values from the store.


```

```using createEntityAdapter

Calling createEntityAdapter gives us an "adapter" object that contains several premade reducer functions, including:

1. addOne / addMany: add new items to the state
2. upsertOne / upsertMany: add new items or update existing ones
3. updateOne / updateMany: update existing items by supplying partial values
4. removeOne / removeMany: remove items based on IDs
5. setAll: replace all existing items

- We can use these functions as case reducers, or as "mutating helpers" inside of createSlice


The adapter also contains:

1. getInitialState: returns an object that looks like { ids: [], entities: {} }, for storing a normalized state of items along with an array of all item IDs
2. getSelectors: generates a standard set of selector functions



const initialState = todosAdapter.getInitialState({
  status: 'idle',
})

const todoSlice = createSlice({
  name: 'todos',
  initialState,
  reducers: {
    todoAdded(state, action) {
      const todo = action.payload
      state.entities[todo.id] = todo
    },
    todoToggled(state, action) {
      const todoId = action.payload
      const todo = state.entities[todoId]

      todo.completed = !todo.completed
    },
    colorSelected: {
      reducer(state, action) {
        const { color, todoId } = action.payload
        state.entities[todoId].color = color
      },
      prepare(todoId, color) {
        return {
          payload: { todoId, color },
        }
      },
    },
    todoDeleted: todosAdapter.removeOne, // here we used it to remove and entity by id
    allTodosCompleted(state, action) {
      Object.values(state.entities).forEach((todo) => {
        todo.completed = true
      })
    },
    completedTodosCleared(state, action) {
      const completedIds = Object.values(state.entities)
        .filter((todo) => todo.completed)
        .map((todo) => todo.id)
      todosAdapter.removeMany(state, completedIds)
    },
    todosLoaded(state, action) {
      const newEntities = {}

      action.payload.forEach((todo) => {
        newEntities[todo.id] = todo
      })

      state.entities = newEntities
      state.status = 'idle'
    },

    todosLoading(state, action) {
      state.status = 'loading'
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchTodos.pending, (state, action) => {
        state.status = 'loading'
      })
      .addCase(fetchTodos.fulfilled, (state, action) => {
        const newEntities = {}

        action.payload.forEach((todo) => {
          newEntities[todo.id] = todo
        })

        state.entities = newEntities
        state.status = 'idle'
      })
      .addCase(saveNewTodo.pending, (state, action) => {
        state.status = 'loading'
      })
      .addCase(saveNewTodo.fulfilled, todosAdapter.addOne)
  },
})


- The different adapter reducer functions take different values depending on the function, all in action payload. The "add" and "upsert" functions take a single item or an array of items, the "remove" functions take a single ID or array of IDs, and so on.

- getInitialState allows us to pass in additional state fields that will be included. In this case, we've passed in a status field, giving us a final todos slice state of {ids, entities, status}, much like we had before.


- We can also replace some of our todos selector functions as well. The getSelectors adapter function will generate selectors like selectAll, which returns an array of all items, and selectById, which returns one item

- However, since getSelectors doesn't know where our data is in the entire Redux state tree, we need to pass in a small selector that returns this slice out of the whole state tree

- if you're using getSelectors from entity adapter, be sure to use setAll as well,

const newEntities = {}

        action.payload.forEach((todo) => {
          newEntities[todo.id] = todo
        })

        state.entities = newEntities
        console.log(state, 'before')
        // todosAdapter.setAll(state, action.payload)
        console.log(state, 'AFTER')
        state.status = 'idle'
      })

if you're setting the state this way, selectAll and selectById from entity adapter might not work
if you're not setting state using setAll, creating a selector manually will still work
```
