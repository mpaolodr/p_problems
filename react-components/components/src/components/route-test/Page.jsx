import React from 'react';

import styled from 'styled-components';

const Container = styled.div`
  height: 100vh;
  background-color: tomato;
  display: flex;
  align-items: center;
  justify-content: center;
`;

export default function Page() {
  return (
    <Container>
      <h2 style={{ fontSize: '5rem' }}>Page</h2>
    </Container>
  );
}
