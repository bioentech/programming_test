Stock Prices
============

You are given a list of stocks and their daily closing prices for a given period.

Your task is to determine which pair of stocks had the most highly (linearly) correlated daily percentage changes of closing prices.

For example, with the sample data below the function should return ['FB', 'MSFT'].

------------------------------------------
| DAY |  GOOG  |   FB   | MSFT  |  AAPL  |
------------------------------------------
|  1  | 742.66 | 108.40 | 55.40 | 106.00 |
|  2  | 738.40 | 107.92 | 54.63 | 104.66 |
|  3  | 738.22 | 109.64 | 54.98 | 104.87 |
|  4  | 741.16 | 112.22 | 55.88 | 105.69 |
|  5  | 739.98 | 109.57 | 54.12 | 104.22 |
|  6  | 747.28 | 113.82 | 59.16 | 110.16 |
|  7  | 746.22 | 114.03 | 58.14 | 109.84 |
|  8  | 741.80 | 112.24 | 55.97 | 108.86 |
|  9  | 745.33 | 114.68 | 61.20 | 110.14 |
| 10  | 741.29 | 112.92 | 57.14 | 107.66 |
| 11  | 742.83 | 113.28 | 56.62 | 108.08 |
| 12  | 750.50 | 115.40 | 59.25 | 109.90 |
------------------------------------------
