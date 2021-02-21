const initState = {
  status: 'ALL',
  colors: [],
};

const filtersReducer = (state = initState, action) => {
  switch (action.type) {
    case 'filters/statusFilterChanged':
      return {
        ...state,
        status: action.payload,
      };
    default:
      return state;
  }
};

export default filtersReducer;
