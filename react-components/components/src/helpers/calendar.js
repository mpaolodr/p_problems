export const THIS_YEAR = +new Date().getFullYear();

// months usually start from 0, thus + 1
export const THIS_MONTH = +new Date().getMonth() + 1;

export const WEEK_DAYS = {
  Sunday: 'Sun',
  Monday: 'Mon',
  Tuesday: 'Tue',
  Wednesday: 'Wed',
  Thursday: 'Thu',
  Friday: 'Fri',
  Saturday: 'Sat',
};

export const CALENDAR_MONTHS = {
  January: 'Jan',
  February: 'Feb',
  March: 'Mar',
  April: 'Apr',
  May: 'May',
  June: 'Jun',
  July: 'Jul',
  August: 'Aug',
  September: 'Sep',
  October: 'Oct',
  November: 'Nov',
  December: 'Dec',
};

// number of weeks in calendar
export const CALENDAR_WEEKS = 6;

// adds a leading 0 until length is reached
export function zeroPad(value, length) {
  return `${value}`.padStart(length, '0');
}

// num of days in a month for a given year
export function getMonthDays(month = THIS_MONTH, year = THIS_YEAR) {
  const months30 = [4, 6, 9, 11];
  const leapYear = year % 4 === 0;

  if (month === 2) {
    if (leapYear) {
      return 29;
    }

    return 28;
  } else {
    if (months30.includes(month)) {
      return 30;
    }

    return 31;
  }
}

// export function getMonthFirstDay(month = THIS_MONTH, year = THIS_YEAR) {
//   return +new Date(`${year}-${zeroPad(month, 2)}-01`).getDay() + 1;
// }

export const getMonthFirstDay = (month = THIS_MONTH, year = THIS_YEAR) => {
  const test = +new Date(`${year}-${zeroPad(month, 2)}-01`).getDay() + 1;

  return +new Date(`${year}-${zeroPad(month, 2)}-01`).getDay() + 1;
};

export function isValidDate(date) {
  const isDate = Object.prototype.toString.call(date) === '[object Date]';
  const isValid = date && !Number.isNaN(date.valueOf());

  return isDate && isValid;
}

// check if two date values are of the same month and year
export function isSameMonth(date, baseDate = new Date()) {
  if (!(isValidDate(date) && isValidDate(baseDate))) return false;

  const baseDateMonth = +baseDate.getMonth() + 1;
  const baseDateYear = baseDate.getFullYear();

  const dateMonth = +date.getMonth() + 1;
  const dateYear = date.getFullYear();

  return +baseDateMonth === +dateMonth && +baseDateYear === +dateYear;
}

export function isSameDay(date, baseDate = new Date()) {
  if (!(isValidDate(date) && isValidDate(baseDate))) return false;

  const baseDateDate = baseDate.getDate();
  const baseDateMonth = +baseDate.getMonth() + 1;
  const baseDateYear = baseDate.getFullYear();

  const dateDate = date.getDate();
  const dateMonth = +date.getMonth() + 1;
  const dateYear = date.getFullYear();

  return (
    +baseDateDate === +dateDate &&
    +baseDateMonth === +dateMonth &&
    +baseDateYear === +dateYear
  );
}

export function getDateISO(date = new Date()) {
  if (!isValidDate(date)) return null;

  return [
    zeroPad(+date.getMonth() + 1, 2),
    zeroPad(+date.getDate(), 2),
    date.getFullYear(),
  ].join('-');
}

export function getPreviousMonth(month, year) {
  const prevMonth = month > 1 ? month - 1 : 12;
  const prevMonthYear = month > 1 ? year : year - 1;

  return { month: prevMonth, year: prevMonthYear };
}

export function getNextMonth(month, year) {
  const nextMonth = month < 12 ? month + 1 : 1;
  const nextMonthYear = month < 12 ? year : year + 1;

  return { month: nextMonth, year: nextMonthYear };
}

// Main function
export default (month = THIS_MONTH, year = THIS_YEAR) => {
  // 1. get number of days in a month and the month's first day
  const monthDays = getMonthDays(month, year);
  const monthFirstDay = getMonthFirstDay(month, year);

  // 2. get number of days from prev and next month to be displayed
  const daysFromPrevMonth = monthFirstDay - 1;
  const daysFromNextMonth =
    CALENDAR_WEEKS * 7 - (daysFromPrevMonth + monthDays);

  // 3. get prev and next months and years
  const { month: prevMonth, year: prevMonthYear } = getPreviousMonth(
    month,
    year
  );
  const { month: nextMonth, year: nextMonthYear } = getNextMonth(month, year);

  // 4. get number of days in previous month
  const prevMonthDays = getMonthDays(prevMonth, prevMonthYear);

  // 5. build dates to be displayed from previous month
  const prevMonthDates = [...new Array(daysFromPrevMonth)].map((n, index) => {
    const day = index + 1 + (prevMonthDays - daysFromPrevMonth);
    return [prevMonthYear, zeroPad(prevMonth, 2), zeroPad(day, 2)];
  });

  // 6. Builds dates to be displayed from current month
  const currentMonthDates = [...new Array(monthDays)].map((n, index) => {
    const day = index + 1;
    return [year, zeroPad(month, 2), zeroPad(day, 2)];
  });

  // 7. Builds dates to be displayed from next month

  const nextMonthDates = [...new Array(daysFromNextMonth)].map((n, index) => {
    const day = index + 1;
    return [nextMonthYear, zeroPad(nextMonth, 2), zeroPad(day, 2)];
  });

  // Combines all dates from previous, current and next months
  return [...prevMonthDates, ...currentMonthDates, ...nextMonthDates];
};
