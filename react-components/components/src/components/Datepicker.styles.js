import styled from 'styled-components';

const Container = styled.div`
  position: relative;
  width: 15%;
`;

const InputContainer = styled.div`
  width: 100%;
  display: flex;
  align-items: center;
  font-size: 1.1rem;
  padding: 0.2em 0.3em;

  .input-field {
    border: 1px solid transparent;
    text-align: center;
  }
`;

const CalendarContainer = styled.div`
  width: 300px;
  height: 300px;
  position: absolute;
  top: 0;
  left: 100%;
  font-size: 1rem;
`;

export { Container, InputContainer, CalendarContainer };
