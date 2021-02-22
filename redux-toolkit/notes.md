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
