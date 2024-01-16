'''
Fabian Campos 
CSC 110 
Programming Project 3
This program covers the user's finances.
'''

def wheres_the_money(salary, mortgage, bills, food, travel):

    salary *= 1
    mortgage *= 12 
    bills *= 12
    food *= 52
    travel *= 1

    tax_percentage = 0

    if salary > 0 and salary < 15000: 
        tax_percentage = 0.10
    elif salary > 15000 and salary < 75000: 
        tax_percentage = 0.20
    elif salary > 75000 and salary < 200000:
        tax_percentage = 0.25
    elif salary > 200000: 
        tax_percentage = 0.30
    
    print("-----------------------------------------------------------------")
    print("See the financial breakdown below, based on a salary of $" + str(salary))
    print("-----------------------------------------------------------------")
    print("| mortage/rent | $" + str(round(mortgage), 2))
    print("|        bills | $" + str(round(bills), 2))
    print("|         food | $" + str(round(food), 2))
    print("|       travel | $" + str(round(travel), 2)) 
    print("|          tax | $" + str(round(tax_percentage * salary), 2))
    print("|        extra | $")
    print("-----------------------------------------------------------------")


wheres_the_money(40000, 2000, 300, 150, 4000)

    

    
    





