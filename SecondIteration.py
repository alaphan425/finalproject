class Business:
    def income(self, quantity, business_income):
        business_income.append[quantity]
        
    def expenditure(self, quantity, business_losses):
        business_losses.append[quantity]
    
    def profits(self,business_income, business_losses, netIncome, business_profits):
        for i in range (len(business_income)):
            business_profits.append[float(business_income[i])-float(business_income[i])]

def main():
    commands = Business()
    business_income = []
    business_losses = []
    business_profits = []
    end = False
    while end == False:
        print("                                      ")
        print("Please select one of the commands below:")
        print("1 - Revenue Input")
        print("2 - Expenditure Input")
        """print("3 - Calculate Net Income")"""
        print("0 - Exit Program")
        print("                                      ")
        selectedOption = str(input())
        
        if selectedOption == "0":
            print("Exiting.")
            end = True
            break
        
        elif selectedOption == "1":
            quantity = input("Input Value of Gross Income")
            commands.income(quantity, business_income)
            
        elif selectedOption == "2":
            quantity = input("Input Value of Expenses")
            commands.expenditure(quantity, business_losses)
            
        """"elif selectedOption == "3":"""
            
            

main()