import React from 'react';

import styled from 'styled-components';

const Circle = styled.div`
  width: 0.8em;
  height: 0.8em;
  border-radius: 50%;
  background: ${(props) => props.color};
`;

const CircleComp = ({ color, position }) => {
  return (
    <Circle
      color={color}
      className={position === 1 ? 'first' : position === 2 ? 'second' : 'third'}
    ></Circle>
  );
};

export default CircleComp;
