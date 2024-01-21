'''
Fabian Campos 
CSC 110 
Programming Project 3
This program covers the user's finances.
'''

def wheres_the_money(salary, mortgage, bills, food, travel):
    '''
    This function creates a table breaking down the user's finances. 
    Args: 
        salary: The user's yearly salary (int).
        mortgage: The user's mortgage expense due monthly (int).
        bills: The user's bills expenses due monthly (int).
        food: The user's food expenses due weekly (int).
        travel: The user's yearly travel expense (int).
    Returns:
        A table calculating the user's total mortgage, bills, 
        food, and travel expenses every year (str).
    '''

    salary *= 1
    mortgage *= 12
    bills *= 12
    food *= 52
    travel *= 1

    tax_percentage = 0

    # tax thresholds according to user's salary

    if salary > 0 and salary < 15000: 
        tax_percentage = 0.10
    elif salary > 15000 and salary < 75000: 
        tax_percentage = 0.20
    elif salary > 75000 and salary < 200000:
        tax_percentage = 0.25
    elif salary > 200000: 
        tax_percentage = 0.30
        
    calculate_tax = tax_percentage * salary

    extra = salary - mortgage - bills - food - travel - calculate_tax
    
    table = ("----------------------------------------------------------------------------\n")
    table += ("See the financial breakdown below, based on a salary of $" + str(salary) + "\n")
    table += ("----------------------------------------------------------------------------\n")
    table += ("| mortgage/rent | $  " + '${:,.2f}'.format(mortgage) + " | " + str(round(mortgage / salary * 100, 1)) + "% |\n")
    table += ("|         bills | $   " + '${:,.2f}'.format(bills) + " |  " + str(round(bills / salary * 100, 1)) + "% |\n")
    table += ("|          food | $   " + '${:,.2f}'.format(food) + " | " + str(round(food / salary * 100, 1)) + "% |\n")
    table += ("|        travel | $   " + '${:,.2f}'.format(travel) + " | " + str(round(travel / salary * 100, 1)) + "% |\n")
    table += ("|           tax | $   " + '${:,.2f}'.format(calculate_tax) + " | " + str(round(calculate_tax / salary * 100, 1)) + "% | " + "#" * int(calculate_tax // salary) + "\n") 
    table += ("|         extra | $  " + '${:,.2f}'.format(extra)  + " | " + str(round(extra / salary * 100, 1)) + "% | " + "#" * int(extra // salary) + "\n")
    table += ("----------------------------------------------------------------------------")

    # determines if user reaches tax limit

    if calculate_tax >= 75000:
        table += (">>> TAX LIMIT REACHED <<<")
        table += ("Overspending")

    print(table)

wheres_the_money(40000, 2000, 300, 150, 4000)




    

    
    





