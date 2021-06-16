from date import Date


if __name__ == '__main__':

    d1 = Date(4, 5, 2020)
    d2 = Date(6, 25, 2020)

    # Assignement 1
    print(d1)

    print(f"This month is: {d1.monthName()}")

    print(f"Is this year leap? {d1.isLeapYear()}")

    print(f"Between the two dates {d1} and {d2} there are {d1.numDays(d2)} days")

    skipDays = 5
    print(f"After {skipDays} days will be the {d1.advanceBy(skipDays)}")

    # Assignement 2
    print(f"This day falls on a {d1.dayOfWeekName()}")

    print(f"This is the {d1.dayOfYear()} day of the year")

    print(f"Is this a weekday? {d1.isWeekday()}")

    print(f"Is this an equinox day? {d1.isEquinox()}")

    print(f"Is this a solstice day? {d1.isSolstice()}")

    print(f"This date {d1}, can be printed also in this format: {d1.asGregorian('|+|')}")

    # Assignement 3
    print()
    d1.printCalendar()

    # Assignement 4
    d3 = Date(month=3, year=1999)

    print(f"\n\n{d3}")