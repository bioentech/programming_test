# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import sys

class StockPrices:
    # param prices dict of string to list. A dictionary containing the tickers of the stocks, and each tickers daily prices.
    # returns list of strings. A list containing the tickers of the two most correlated stocks.
    @staticmethod
    def most_corr(prices):
        return None

#For example, with the parameters below the function should return ['FB', 'MSFT'].
prices = {
    'GOOG' : [
        742.66, 738.40, 738.22, 741.16,
        739.98, 747.28, 746.22, 741.80,
        745.33, 741.29, 742.83, 750.50
    ],
    'FB' : [
        108.40, 107.92, 109.64, 112.22,
        109.57, 113.82, 114.03, 112.24,
        114.68, 112.92, 113.28, 115.40
    ],
    'MSFT' : [
        55.40, 54.63, 54.98, 55.88,
        54.12, 59.16, 58.14, 55.97,
        61.20, 57.14, 56.62, 59.25
    ],
    'AAPL' : [
        106.00, 104.66, 104.87, 105.69,
        104.22, 110.16, 109.84, 108.86,
        110.14, 107.66, 108.08, 109.90
    ]
}

def main(argv):
    print(StockPrices.most_corr(prices))



if __name__ == '__main__':
    main(sys.argv[1:])
