import React, { useState, useEffect } from 'react';
import usePrevious from '../hooks/usePrevious';

import Calendar from './Calendar';

import { getDateISO, isValidDate } from '../helpers/calendar';

import calendarIcon from '../assets/calendar.svg';

import {
  Container,
  InputContainer,
  CalendarContainer,
} from './Datepicker.styles';

const Datepicker = (props) => {
  // props
  const { date, label, onDateChanged } = props;

  const [currentDate, setCurrentDate] = useState(null);
  const [calendarOpen, setCalendarOpen] = useState(false);
  const prevDate = usePrevious(date);

  const toggleCalendar = () => {
    // console.log(calendarOpen);
    setCalendarOpen(!calendarOpen);
  };

  const handleChange = (e) => e.preventDefault();

  const handleDateChange = (date) => {
    const newDate = date ? getDateISO(date) : null;

    if (currentDate !== newDate) {
      setCurrentDate(newDate);
      setCalendarOpen(false);

      onDateChanged(newDate);
    }
  };

  useEffect(() => {
    if (date === currentDate) {
      const newDate = date && new Date(date);

      if (isValidDate(newDate)) {
        setCurrentDate(getDateISO(newDate));
      }
    } else {
      const dateISO = getDateISO(new Date(date));
      const prevDateISO = getDateISO(new Date(currentDate));

      if (dateISO !== prevDateISO) {
        setCurrentDate(dateISO);
      }
    }
  }, [date]);

  return (
    <Container>
      <InputContainer>
        <input
          className='input-field'
          type='text'
          value={date ? date.split('-').join(' / ') : ''}
          onChange={handleChange}
          placeholder='YYYY-MM-DD'
          readOnly
        />
        <i className='icon' onClick={toggleCalendar}>
          <img src={calendarIcon} alt='' />
        </i>
      </InputContainer>

      <CalendarContainer>
        {calendarOpen && (
          <Calendar
            date={date && new Date(date)}
            handleDateChange={handleDateChange}
          />
        )}
      </CalendarContainer>
    </Container>
  );
};

export default Datepicker;
