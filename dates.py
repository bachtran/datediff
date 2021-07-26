class Date:
    '''Represent a date'''
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return "{:02}/{:02}/{}".format(self.day, self.month, self.year)

    @classmethod
    def parse_date(cls, date_string):
        '''Expect date_string dd/mm/yyyy. Does not validate.'''
        d, m, y = date_string.split('/')
        return cls(int(d), int(m), int(y))

def is_leap_year(year):
    '''Decide whether a given year is a leap year'''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def list_year_month(d1, d2):
    '''Return a list of (month, year) in the date range'''
    start, end = validate_date_range(d1, d2)
    result = []

    for year in range(start.year, end.year+1):
        if year == start.year:
           start_m = start.month
           end_m = 12 if year != end.year else end.month
        elif year == end.year:
           start_m = 1
           end_m = end.month
        else:
           start_m = 1
           end_m = 12
        for month in range(start_m, end_m + 1):
            result.append((month, year))
    return result

mmap = (31,28,31,30,31,30,31,31,30,31,30,31)

def validate_date_range(d1, d2):
    '''Return (start_date, end_date)'''
    if d1.year > d2.year:
        return d2, d1
    elif d1.year < d2.year:
        return d1, d2
    else:
        if d1.month > d2.month:
            return d2, d1
        elif d1.month < d2.month:
            return d1, d2
        else:
            if d1.day > d2.day:
                return d2, d1
            else:
                return d1, d2

def calculate_date_diff(d1, d2):
    '''Calculate date difference between d1 and d2'''
    sum = 0
    start, end = validate_date_range(d1, d2)
    # Calculate day counts with whole months
    for item in list_year_month(start, end):
        month = item[0]
        year = item[1]
        if is_leap_year(year) and month == 2:
            sum = sum + 29
        else:
            sum = sum + mmap[month-1]
    # Take into account start's and end's month days. Also not counting first and last day (-1)
    sum = sum - start.day - (mmap[end.month-1] - end.day) - 1
    return sum
