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
