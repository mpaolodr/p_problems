import React from 'react';

import styled from 'styled-components';

const Container = styled.div`
  height: 100vh;
  background-color: #0ca147;
  display: flex;
  align-items: center;
  justify-content: center;
`;

export default function Home() {
  return (
    <Container>
      <h2 style={{ fontSize: '5rem' }}>Home</h2>
    </Container>
  );
}
