y = int(input("Enter a Year: "))

if y%4 == 0 or y%400 == 0:
    print(f"{y} is a Leap Year!")

else:
    print(f"{y} is not a Leap Year.")