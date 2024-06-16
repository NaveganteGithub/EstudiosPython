import calendar

# El parametro w: para determinar el ancho del calendario
# El parametro l: para determinar la altura del calendario
# El parametro m: para determinar cuantas columnas tendra el calendario
print(calendar.calendar(2024))

"""
                                  2024

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                   1  2  3
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       4  5  6  7  8  9 10
15 16 17 18 19 20 21      12 13 14 15 16 17 18      11 12 13 14 15 16 17
22 23 24 25 26 27 28      19 20 21 22 23 24 25      18 19 20 21 22 23 24
29 30 31                  26 27 28 29               25 26 27 28 29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7             1  2  3  4  5                      1  2
 8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
29 30                     27 28 29 30 31            24 25 26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                         1
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                         1
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                    30 31

"""

print(calendar.calendar(2024, w=4))

"""
                                                       2024

             January                                 February                                 March
Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun
  1    2    3    4    5    6    7                        1    2    3    4                             1    2    3
  8    9   10   11   12   13   14         5    6    7    8    9   10   11         4    5    6    7    8    9   10
 15   16   17   18   19   20   21        12   13   14   15   16   17   18        11   12   13   14   15   16   17
 22   23   24   25   26   27   28        19   20   21   22   23   24   25        18   19   20   21   22   23   24
 29   30   31                            26   27   28   29                       25   26   27   28   29   30   31

              April                                    May                                     June
Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun
  1    2    3    4    5    6    7                   1    2    3    4    5                                  1    2
  8    9   10   11   12   13   14         6    7    8    9   10   11   12         3    4    5    6    7    8    9
 15   16   17   18   19   20   21        13   14   15   16   17   18   19        10   11   12   13   14   15   16
 22   23   24   25   26   27   28        20   21   22   23   24   25   26        17   18   19   20   21   22   23
 29   30                                 27   28   29   30   31                  24   25   26   27   28   29   30

               July                                   August                                September
Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun
  1    2    3    4    5    6    7                        1    2    3    4                                       1
  8    9   10   11   12   13   14         5    6    7    8    9   10   11         2    3    4    5    6    7    8
 15   16   17   18   19   20   21        12   13   14   15   16   17   18         9   10   11   12   13   14   15
 22   23   24   25   26   27   28        19   20   21   22   23   24   25        16   17   18   19   20   21   22
 29   30   31                            26   27   28   29   30   31             23   24   25   26   27   28   29
                                                                                 30

             October                                 November                                December
Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun
       1    2    3    4    5    6                             1    2    3                                       1
  7    8    9   10   11   12   13         4    5    6    7    8    9   10         2    3    4    5    6    7    8
 14   15   16   17   18   19   20        11   12   13   14   15   16   17         9   10   11   12   13   14   15
 21   22   23   24   25   26   27        18   19   20   21   22   23   24        16   17   18   19   20   21   22
 28   29   30   31                       25   26   27   28   29   30             23   24   25   26   27   28   29
                                                                                 30   31

"""

print(calendar.calendar(2024, w=4, l=2))

"""
                                                       2024



             January                                 February                                 March

Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun

  1    2    3    4    5    6    7                        1    2    3    4                             1    2    3

  8    9   10   11   12   13   14         5    6    7    8    9   10   11         4    5    6    7    8    9   10

 15   16   17   18   19   20   21        12   13   14   15   16   17   18        11   12   13   14   15   16   17

 22   23   24   25   26   27   28        19   20   21   22   23   24   25        18   19   20   21   22   23   24

 29   30   31                            26   27   28   29                       25   26   27   28   29   30   31



              April                                    May                                     June

Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun

  1    2    3    4    5    6    7                   1    2    3    4    5                                  1    2

  8    9   10   11   12   13   14         6    7    8    9   10   11   12         3    4    5    6    7    8    9

 15   16   17   18   19   20   21        13   14   15   16   17   18   19        10   11   12   13   14   15   16

 22   23   24   25   26   27   28        20   21   22   23   24   25   26        17   18   19   20   21   22   23

 29   30                                 27   28   29   30   31                  24   25   26   27   28   29   30



               July                                   August                                September

Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun

  1    2    3    4    5    6    7                        1    2    3    4                                       1

  8    9   10   11   12   13   14         5    6    7    8    9   10   11         2    3    4    5    6    7    8

 15   16   17   18   19   20   21        12   13   14   15   16   17   18         9   10   11   12   13   14   15

 22   23   24   25   26   27   28        19   20   21   22   23   24   25        16   17   18   19   20   21   22

 29   30   31                            26   27   28   29   30   31             23   24   25   26   27   28   29

                                                                                 30



             October                                 November                                December

Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun

       1    2    3    4    5    6                             1    2    3                                       1

  7    8    9   10   11   12   13         4    5    6    7    8    9   10         2    3    4    5    6    7    8

 14   15   16   17   18   19   20        11   12   13   14   15   16   17         9   10   11   12   13   14   15

 21   22   23   24   25   26   27        18   19   20   21   22   23   24        16   17   18   19   20   21   22

 28   29   30   31                       25   26   27   28   29   30             23   24   25   26   27   28   29

                                                                                 30   31

"""

print(calendar.calendar(2024, m=2))

"""
                     2024

      January                   February
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4
 8  9 10 11 12 13 14       5  6  7  8  9 10 11
15 16 17 18 19 20 21      12 13 14 15 16 17 18
22 23 24 25 26 27 28      19 20 21 22 23 24 25
29 30 31                  26 27 28 29

       March                     April
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7
 4  5  6  7  8  9 10       8  9 10 11 12 13 14
11 12 13 14 15 16 17      15 16 17 18 19 20 21
18 19 20 21 22 23 24      22 23 24 25 26 27 28
25 26 27 28 29 30 31      29 30

        May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2
 6  7  8  9 10 11 12       3  4  5  6  7  8  9
13 14 15 16 17 18 19      10 11 12 13 14 15 16
20 21 22 23 24 25 26      17 18 19 20 21 22 23
27 28 29 30 31            24 25 26 27 28 29 30

        July                     August
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4
 8  9 10 11 12 13 14       5  6  7  8  9 10 11
15 16 17 18 19 20 21      12 13 14 15 16 17 18
22 23 24 25 26 27 28      19 20 21 22 23 24 25
29 30 31                  26 27 28 29 30 31

     September                  October
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1          1  2  3  4  5  6
 2  3  4  5  6  7  8       7  8  9 10 11 12 13
 9 10 11 12 13 14 15      14 15 16 17 18 19 20
16 17 18 19 20 21 22      21 22 23 24 25 26 27
23 24 25 26 27 28 29      28 29 30 31
30

      November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1
 4  5  6  7  8  9 10       2  3  4  5  6  7  8
11 12 13 14 15 16 17       9 10 11 12 13 14 15
18 19 20 21 22 23 24      16 17 18 19 20 21 22
25 26 27 28 29 30         23 24 25 26 27 28 29
                          30 31

"""

print(calendar.calendar(2024, w=4, l=2, m=2))

"""
                                   2024



             January                                 February

Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun

  1    2    3    4    5    6    7                        1    2    3    4

  8    9   10   11   12   13   14         5    6    7    8    9   10   11

 15   16   17   18   19   20   21        12   13   14   15   16   17   18

 22   23   24   25   26   27   28        19   20   21   22   23   24   25

 29   30   31                            26   27   28   29



              March                                   April

Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun

                      1    2    3         1    2    3    4    5    6    7

  4    5    6    7    8    9   10         8    9   10   11   12   13   14

 11   12   13   14   15   16   17        15   16   17   18   19   20   21

 18   19   20   21   22   23   24        22   23   24   25   26   27   28

 25   26   27   28   29   30   31        29   30



               May                                     June

Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun

            1    2    3    4    5                                  1    2

  6    7    8    9   10   11   12         3    4    5    6    7    8    9

 13   14   15   16   17   18   19        10   11   12   13   14   15   16

 20   21   22   23   24   25   26        17   18   19   20   21   22   23

 27   28   29   30   31                  24   25   26   27   28   29   30



               July                                   August

Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun

  1    2    3    4    5    6    7                        1    2    3    4

  8    9   10   11   12   13   14         5    6    7    8    9   10   11

 15   16   17   18   19   20   21        12   13   14   15   16   17   18

 22   23   24   25   26   27   28        19   20   21   22   23   24   25

 29   30   31                            26   27   28   29   30   31



            September                                October

Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun

                                1              1    2    3    4    5    6

  2    3    4    5    6    7    8         7    8    9   10   11   12   13

  9   10   11   12   13   14   15        14   15   16   17   18   19   20

 16   17   18   19   20   21   22        21   22   23   24   25   26   27

 23   24   25   26   27   28   29        28   29   30   31

 30



             November                                December

Mon  Tue  Wed  Thu  Fri  Sat  Sun       Mon  Tue  Wed  Thu  Fri  Sat  Sun

                      1    2    3                                       1

  4    5    6    7    8    9   10         2    3    4    5    6    7    8

 11   12   13   14   15   16   17         9   10   11   12   13   14   15

 18   19   20   21   22   23   24        16   17   18   19   20   21   22

 25   26   27   28   29   30             23   24   25   26   27   28   29

                                         30   31

"""