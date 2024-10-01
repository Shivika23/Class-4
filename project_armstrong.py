def armstrong_number(number):
    digits = str(number)
    order = len(digits)
    sum_of_powers = 0
    
    for digit in digits:
        sum_of_powers += int(digit) ** order
    
    return sum_of_powers == number

number = int(input("Enter a number to check if it is an Armstrong number: "))

if armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
