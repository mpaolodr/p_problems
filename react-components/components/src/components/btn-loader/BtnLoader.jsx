import React from 'react';

import CircleComp from './Circle';
import styled, { keyframes, css } from 'styled-components';

const bounce = keyframes`

0% {
    transform: translateY(0)
}

100% {
    transform: translateY(-50%)
}

`;

const LdrContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;

  & > :not(:last-child) {
    margin-right: 0.5rem;
  }

  .first {
    animation: ${bounce} 0.3s infinite alternate;
  }

  .second {
    animation: ${bounce} 0.3s infinite alternate 0.25s;
  }

  .third {
    animation: ${bounce} 0.3s infinite alternate 0.5s;
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
