#Design and implement a Money class that stores monetary values in dollars and cents. Special method init
# should have the following function header, def init(self, dollars, cents) Include special method repr
# (str) for displaying values in dollars and cents: $ 0.45, $ 1.00, $ 1.25. Also include special method
# add, and three getter methods that each provide the monetary value in another currency. Choose any three
# currencies to convert to

class Money:
    def __init__(self,dollars,cents):
        self.dollars=dollars
        self.cents=cents
    def __repr__(self,sym):
        self.doll=self.cents/100
        print(self.sym,self.dollars+self.doll)
object=Money(45,10)
object.__repr__("$")