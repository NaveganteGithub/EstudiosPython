import calendar

print(calendar.month(2024, 4))

"""
     April 2024
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
"""

print(calendar.month(2024, 4, w=4))

"""
            April 2024
Mon  Tue  Wed  Thu  Fri  Sat  Sun
  1    2    3    4    5    6    7
  8    9   10   11   12   13   14
 15   16   17   18   19   20   21
 22   23   24   25   26   27   28
 29   30
"""

print(calendar.month(2024, 4, w=4, l=2))

"""
            April 2024

Mon  Tue  Wed  Thu  Fri  Sat  Sun

  1    2    3    4    5    6    7

  8    9   10   11   12   13   14

 15   16   17   18   19   20   21

 22   23   24   25   26   27   28

 29   30

"""

print(calendar.month(2024, 4, w=4, l=2))

"""
            April 2024

Mon  Tue  Wed  Thu  Fri  Sat  Sun

  1    2    3    4    5    6    7

  8    9   10   11   12   13   14

 15   16   17   18   19   20   21

 22   23   24   25   26   27   28

 29   30

"""