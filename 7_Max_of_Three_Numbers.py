a = int(input("Enter 1st number--- "))
b = int(input("Enter 2nd number--- "))
c = int(input("Enter 3rd number--- "))

if a > b and a > c:
    print(f"Among {a}, {b} and {c}\nThe largest number is {a}")

elif b > a and b > c:
    print(f"Among {a}, {b} and {c}\nThe largest number is {b}")

elif c > a and c > b:
    print(f"Among {a}, {b} and {c}\nThe largest number is {c}")    