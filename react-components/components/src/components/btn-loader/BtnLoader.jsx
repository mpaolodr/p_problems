import React from 'react';

import CircleComp from './Circle';
import styled, { keyframes, css } from 'styled-components';

const bounce = keyframes`

0% {
    transform: translateY(0)
}

100% {
    transform: translateY(-20px)
}

`;

const LdrContainer = styled.div`
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  & > :not(:last-child) {
    margin-right: 0.5em;
  }

  .first {
    animation: ${bounce} 0.5s infinite alternate;
  }

  .second {
    animation: ${bounce} 0.5s infinite alternate 0.25s;
  }

  .third {
    animation: ${bounce} 0.5s infinite alternate 0.5s;
  }
`;

const BtnLoader = (props) => {
  const { color } = props;

  return (
    <LdrContainer>
      <CircleComp position={1} color={color} />
      <CircleComp position={2} color={color} />
      <CircleComp position={3} color={color} />
    </LdrContainer>
  );
};

export default BtnLoader;
