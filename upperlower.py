def count_case(string):
    upper_case = sum(1 for c in string if c.isupper())
    lower_case = sum(1 for c in string if c.islower())
    return upper_case, lower_case

string = input("Enter a string: ")
upper_case, lower_case = count_case(string)
print(f"Upper case letters: {upper_case}")
print(f"Lower case letters: {lower_case}")