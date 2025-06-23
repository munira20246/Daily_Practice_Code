v = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
given_num = input("Enter a Character--- ")

if given_num in v:
    print(f"{given_num.upper()} is a Vowel.")

else:
    print(f"{given_num.upper()} is a Consonant.")