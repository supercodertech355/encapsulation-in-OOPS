class computer:

    def __init__(self):
        self.__maxprice = 50000

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setmaxprice(self,price):
        self.__maxprice = price


c = computer()
c.sell()

c.__maxprice = 100001
c.sell()

c.setmaxprice(1000011)
c.sell()