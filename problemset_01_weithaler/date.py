from datetime import datetime


class Date:
    # Creates an object instance for the specified Gregorian date.
    def __init__(self, month=None, day=None, year=None):

        if month is None:
            month = datetime.today().month

        if day is None:
            day = datetime.today().day

        if year is None:
            year = datetime.today().year

        self._julianDay = 0
        assert self.isValidGregorian(month, day, year), "Invalid Gregorian date."
        # The first line of the equation, T = (M - 14) / 12, has to be changed
        # since Python's implementation of integer division is not the same
        # as the mathematical definition.
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + (1461 * (year + 4800 + tmp) // 4) + (367 * (month - 2 - tmp * 12) // 12) - (
                3 * ((year + 4900 + tmp) // 100) // 4)

    # Extracts the appropriate Gregorian date component.
    def month(self):

        return (self.toGregorian())[0]  # returning M from (M, d, y)

    def day(self):

        return (self.toGregorian())[1]  # returning D from (m, D, y)

    def year(self):

        return (self.toGregorian())[2]  # returning Y from (m, d, Y)

    # Returns day of the week as an int between 0 (Mon) and 6 (Sun).
    def dayOfWeek(self):
        month, day, year = self.toGregorian()
        if month < 3:
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day + year + year // 4 - year // 100 + year // 400) % 7

    # Returns the date as a string in Gregorian format.
    def __str__(self):
        month, day, year = self.toGregorian()
        return "%02d/%02d/%04d" % (month, day, year)

    # Logically compares the two dates.
    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay

    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay

    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay

    def __gt__(self, otherDate):
        return self._julianDay > otherDate._julianDay

    def __ge__(self, otherDate):
        return self._julianDay >= otherDate._julianDay

    def toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year

    # Assignment 1

    def monthName(self):
        monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']
        return monthNames[self.month() - 1]

    def isLeapYear(self):
        return self.year() % 4 == 0 and (self.year() % 100 != 0 or self.year() % 400 == 0)

    def numDays(self, otherDate):
        return abs(self._julianDay - otherDate._julianDay)

    def advanceBy(self, nDays):
        self._julianDay += nDays
        if self._julianDay < 0:
            self._julianDay = 0
        return self.toGregorian()

    def isValidGregorian(self, month=None, day=None, year=None):

        if month is None:
            month = self.month()

        if day is None:
            day = self.day()

        if year is None:
            year = self.year()

        if 0 < year:
            if 1 <= month <= 12:
                if month == 2:
                    if (0 < day <= 29 and self.isLeapYear()) or 0 < day <= 28:
                        return True
                elif (month < 8 and month % 2 == 1) or (month >= 8 and month % 2 == 0):
                    if 0 < day <= 31:
                        return True
                else:
                    if 0 < day <= 30:
                        return True
        return False

    # Assignment 2

    def dayOfWeekName(self):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days[self.dayOfWeek()]

    def dayOfYear(self):
        return self.numDays(Date(1, 1, self.year())) + 1

    def isWeekday(self):
        return 0 <= self.dayOfWeek() <= 4

    def isEquinox(self):
        return True if (self.day() == 20 and self.month() == 3) or (self.day() == 22 and self.month() == 9) else False

    def isSolstice(self):
        return True if self.day() == 21 and (self.month() == 6 or self.month() == 12) else False

    def asGregorian(self, divchar='/'):
        month, day, year = self.toGregorian()
        return f"%02d{divchar}%02d{divchar}%04d" % (month, day, year)

    def printCalendar(self):
        print(f'\t  {self.monthName()} {self.year()}\nSu\tMo\tTu\tWe\tTh\tFr\tSa')

        dateArray = []
        spaces = [1, 2, 3, 4, 5, 6, 0]

        startingDate = Date(self.month(), 1, self.year())

        for i in range(spaces[startingDate.dayOfWeek()]):
            dateArray.append(' ')

        while self.month() == startingDate.month():
            dateArray.append(startingDate.day())
            startingDate.advanceBy(1)

        for index, e in enumerate(dateArray):
            print(f'{e}\t', end='')
            if index % 7 == 6:
                print()
