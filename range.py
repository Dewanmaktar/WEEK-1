def is_in_range(num, start, end):
    return start <= num <= end

number = int(input("Enter a number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if is_in_range(number, start, end):
    print(f"{number} is in the range {start} to {end}")
else:
    print(f"{number} is not in the range {start} to {end}")