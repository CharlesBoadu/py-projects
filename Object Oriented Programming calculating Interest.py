class Investment:

    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest


    def value_after(self, n):
        value_after_n_years = self.principal * (1 + self.interest) ** n
        return value_after_n_years
    
    def __str__(self):
        print(str('principal  -  ${:.2f}'.format(self.principal))+',', 'Interest Rate  -  {:.2f}%'.format(self.interest))
        

e = Investment(1000, 5.12)
e.__str__()
print("Value after 2 years is ${:.2f}".format(e.value_after(2)))
