def add(a, b):
  print(f"The Sum of ({int(a)} + {int(b)}) is {a + b}")

def subt(x, y):
  print(f"The difference between two ({int(x)} - {int(y)}) is {x - y}")

def mult(n, m):
  print(f"The Product of ({int(m)} * {int(n)}) is {n * m}")  

def div(k, p):
  print(f"The the result of dividing ({int(k)}/{int(p)}) is {k / p}")

  print("Welcome to the calculator system.")
print('1. add--Press(+)')
print('2. subtract--Press(-)')
print('3. multiply--Press(*)')
print('4. divide--Press(/)')
print('5. exit--Press(x)')

def calculator():
   closing = False
   while not closing:
      choice = input("Give an input you want: ")
      try:
       if choice == 'x': 
        closing = True 
       if choice in ['+', '-', '*', '/']:
         num1 = float(input("Enter 1st valid number: "))
         num2 = float(input("Enter 2nd valid number: "))
       
         if choice == '+':
           add(num1, num2)
          
         elif choice == '-':
          subt(num1, num2)
         
         elif choice == '*':
           mult(num1, num2)

         elif choice == '/':
           div(num1, num2)
           
       else:
        print("Enter a valid number between (1-4)")

      except (ValueError, ZeroDivisionError, SyntaxError, RuntimeError, TypeError) as e:
        print('Error', e)
        
      finally:
        print("Okay")      

calculator()