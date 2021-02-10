import React, { useState, useEffect } from 'react';
import usePrevious from '../hooks/usePrevious';

import calendar, {
  isValidDate,
  isSameDay,
  isSameMonth,
  getDateISO,
  getNextMonth,
  getPreviousMonth,
  WEEK_DAYS,
  CALENDAR_MONTHS,
  CALENDAR_WEEKS,
} from '../helpers/calendar';

import {
  ArrowLeft,
  ArrowRight,
  CalendarContainer,
  CalendarHeader,
  CalendarGrid,
  CalendarMonth,
  CalendarCell,
  CalendarDay,
  CalendarDate,
  HighlightedCalendarDate,
  TodayCalendarDate,
} from './Calendar.styles';

const Calendar = (props) => {
  const [currentDate, setCurrentDate] = useState(() => {
    const isDateObject = isValidDate(props.date);
    const _date = isDateObject ? props.date : new Date();

    return {
      current: isDateObject ? props.date : null,
      month: +_date.getMonth() + 1,
      year: _date.getFullYear(),
      today: new Date(),
    };
  });
  const prevDate = usePrevious(props.date);

  const resolveStateFromDate = (date) => {
    const isDateObject = isValidDate(date);
    const _date = isDateObject ? date : new Date();

    return {
      current: isDateObject ? date : null,
      month: +_date.getMonth() + 1,
      year: _date.getFullYear(),
      today: new Date(),
    };
  };

  useEffect(() => {
    const now = new Date();
    const tomorrow = new Date().setHours(0, 0, 0, 0) + 24 * 60 * 60 * 1000;
    const ms = tomorrow - now;

    setCurrentDate({ ...currentDate, today: new Date() });

    if (props.date !== prevDate) {
      const { date, onDateChanged } = props;
      const prevdate = prevDate;

      const dateMatch = date === prevdate || isSameDay(date, prevdate);

      !dateMatch &&
        setCurrentDate(resolveStateFromDate(date), () => {
          typeof onDateChanged === 'function' && onDateChanged(date);
        });
    }
  }, [props.date]);

  const goToDate = (date) => (event) => {
    event && event.preventDefault();

    const { current } = currentDate;
    const { onDateChanged } = props;

    !(current && isSameDay(date, current)) &&
      setCurrentDate(resolveStateFromDate(date), () => {
        typeof onDateChanged === 'function' && onDateChanged(date);
      });
  };

  const goToPreviousMonth = () => {
    const { month, year } = currentDate;
    const { month: newMonth, year: newYear } = getPreviousMonth(month, year);
    setCurrentDate({ ...currentDate, month: newMonth, year: newYear });
  };

  const goToNextMonth = () => {
    const { month, year } = currentDate;
    const { month: newMonth, year: newYear } = getNextMonth(month, year);
    setCurrentDate({ ...currentDate, month: newMonth, year: newYear });
  };

  const goToPreviousYear = () => {
    const { year } = currentDate;
    setCurrentDate({ ...currentDate, year: year - 1 });
  };

  const goToNextYear = () => {
    const { year } = currentDate;
    setCurrentDate({ ...currentDate, year: year + 1 });
  };

  const handlePrevious = (e) => {
    e && e.preventDefault();
    const fn = e.shiftKey ? goToPreviousYear : goToPreviousMonth;
    fn();
  };

  const handleNext = (e) => {
    e && e.preventDefault();
    const fn = e.shiftKey ? goToNextYear : goToNextMonth;
    fn();
  };

  const getCalendarDates = () => {
    const { current, month, year } = currentDate;
    const calendarMonth = month || +current.getMonth() + 1;
    const calendarYear = year || current.getFullYear();

    return calendar(calendarMonth, calendarYear);
  };

  const renderMonthAndYear = () => {
    const { month, year } = currentDate;

    const monthName = Object.keys(CALENDAR_MONTHS)[
      Math.max(0, Math.min(month - 1, 11))
    ];

    return (
      <CalendarHeader>
        <ArrowLeft
          className='arrow-left'
          onMouseDown={handlePrevious}
          title='Previous Month'
        />

        <CalendarMonth className='calendar-month'>
          {monthName} {year}
        </CalendarMonth>

        <ArrowRight
          className='arrow-right'
          onMouseDown={handleNext}
          title='Next Month'
        />
      </CalendarHeader>
    );
  };

  const renderDayLabel = (day, index) => {
    const dayLabel = WEEK_DAYS[day].toUpperCase();

    return (
      <CalendarDay key={dayLabel} index={index}>
        {dayLabel}
      </CalendarDay>
    );
  };

  return (
    <CalendarContainer>
      {renderMonthAndYear()}
      <CalendarGrid>
        <>
          {Object.keys(WEEK_DAYS).map((day, index) =>
            renderDayLabel(day, index)
          )}
        </>

        <>
          {getCalendarDates().map((date, index) => {
            const { current, month, year, today } = currentDate;
            const _date = new Date(date.join('-'));

            const isToday = isSameDay(_date, today);
            const isCurrent = current && isSameDay(_date, current);
            const isMonth =
              month &&
              year &&
              isSameMonth(_date, new Date([year, month, 1].join('-')));

            const onClick = goToDate(_date);

            const properties = {
              index,
              isMonth,
              onClick,
              title: _date.toDateString(),
            };

            return (
              <>
                {isCurrent ? (
                  <HighlightedCalendarDate {...properties}>
                    {_date.getDate()}
                  </HighlightedCalendarDate>
                ) : isToday ? (
                  <TodayCalendarDate {...properties}>
                    {_date.getDate()}
                  </TodayCalendarDate>
                ) : (
                  <CalendarDate {...properties}>{_date.getDate()}</CalendarDate>
                )}
              </>
            );
          })}
        </>
      </CalendarGrid>
    </CalendarContainer>
  );
};

export default Calendar;
