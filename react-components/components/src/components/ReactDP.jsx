import React, { useState } from 'react';
import Datepicker from 'react-datepicker';
import styled from 'styled-components';
import 'react-datepicker/dist/react-datepicker.css';

const CalendarContainer = styled.div`
  font-size: 0.9rem;
  border: 2px solid #0ca17d;
  border-radius: 5px;
  overflow: hidden;
  background: white;
`;

const Test = styled.div`
  .green {
    background: #0ca17d;
    border-radius: 3px;
    color: red;
  }
`;

export default function ReactDp() {
  //   const [bday, setBday] = useState(new Date('1992-02-05T00:00:00.000'));

  //   const Container = ({ className, children }) => {
  //     return <CalendarContainer>{children}</CalendarContainer>;
  //   };

  //   return (
  //     <Datepicker
  //       selected={bday}
  //       onChange={(date) => setBday(date)}
  //       calendarContaine={Container}
  //     />
  //   );

  const [startDate, setStartDate] = useState(
    new Date('1992-02-05T00:00:00.000')
  );
  const Container = ({ className, children }) => {
    return (
      <CalendarContainer className={className}>
        <div style={{ position: 'relative' }}>{children}</div>
      </CalendarContainer>
    );
  };
  return (
    <Test>
      <Datepicker
        selected={startDate}
        onChange={(date) => setStartDate(date)}
        calendarContainer={Container}
        openToDate={startDate}
        dayClassName={(date) => (date === startDate ? 'green' : 'blue')}
      />
    </Test>
  );
}
