class StockSpanner:

    def __init__(self):
        self.lst = [(0, inf)]                   # (price, date)

    def next(self, price: int) -> int:          
        date = self.lst[0][0] + 1               # current date
        while self.lst[0][1] <= price:          # pop every days before with smaller price
            self.lst.pop(0)                  
        self.lst.insert(0, (date, price))       # insert current price and dates
        return self.lst[0][0] - self.lst[1][0]  # result is distance of first two dates