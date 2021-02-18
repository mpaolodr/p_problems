import React from 'react';

const Test = (props) => {
  return (
    <div>
      <input
        type='text'
        value={props.text}
        onChange={(e) => props.changer(e.target.value)}
      />
    </div>
  );
};

export default Test;
