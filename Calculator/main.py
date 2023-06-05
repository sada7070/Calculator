from art import logo
print(logo)

def add(n1, n2):
  return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2


def calculation():
  first_no=eval(input("What's the first number?: "))
  operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div 
  }
  
  for key in operations:
    print(key)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick  an opearation from above to perform: ")
    second_no=eval(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer= calculation_function(first_no, second_no)
  
    print(f"{first_no} {operation_symbol} {second_no} = {answer}")
    
    
    if input(f"Type 'y' to continue calculating with {answer}, type 'n' to start new calculation: ") =="y":
      first_no=answer
    else:
      should_continue=False
      calculation()
      

calculation()