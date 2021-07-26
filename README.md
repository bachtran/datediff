Date diff
===

The code is written in Python3. The base runtime of Python3+ is needed to run the code.

To run the main script:

```bash
python3 main.py 03/01/1989 03/08/1983
```

To run tests:

```bash
python3 -m unittest
```

The implementation of the date difference calculation is in `dates.py`


The ideas:
---

- The approach I choose is to consider the whole months in the date period, then take into account the day in the start's and end's months. Lastly, I substract a day from the total as the first and last day are partial days and not counted. `dates.list_year_month()` and `dates.calculate_date_diff()`
- The handling of leap year is also necessary. `dates.is_leap_year()`
- To deal with date input of either `start-end` or `end`-`start`, a validation function `dates.validate_date_range()` rearranges the order to `start-end`
- A class to represent date for convenience. `dates.Date`
