#  ex1 - function to add two number
"""def add_func(a,b):
    total = a+b
    print(total)
    return total
add_func(7,9)
"""
# example 2- function to determine if given state has no sales tax
def has_no_sales_tax(state):
    states_with_no_sales_tax = ["Alaska","Oregon","Florida","Montana","Maryland"]
    no_tax = None
    if state.upper() in states_with_no_sales_tax :
     no_tax = True
    else:
        no_tax = False
    return no_tax
user_state = "Califiornia"
tax = has_no_sales_tax(user_state)
print(tax)



