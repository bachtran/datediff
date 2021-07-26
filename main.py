import argparse

import dates

parser = argparse.ArgumentParser(description='Calculate difference between dates.')
parser.add_argument('dates', nargs=2, help='Dates for difference calculation.')

args = parser.parse_args()

date1 = dates.Date.parse_date(args.dates[0])
date2 = dates.Date.parse_date(args.dates[1])

print('{} - {}: {}'.format(date1, date2, dates.calculate_date_diff(date1, date2)))
