from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2
  
#Divide
def divide(n1, n2):
  return n1 / n2

#Dict for calc operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))
  for key in operations:
    print(key)
  end_calculations = False
  
  while not end_calculations:
    operation_key = input("Pick an operation from the line above: ")
    num2 = float(input("What is the next number?: "))
    operation_function = operations[operation_key]
    answer = operation_function(num1, num2)
    print(f"{num1} {operation_key} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start again: ").lower() == "y":
      num1 = answer
    else:
      end_calculations = True
      calculator()

calculator()