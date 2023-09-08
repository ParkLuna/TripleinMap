try:
    input_numbers = input("Enter a list of integers separated by spaces: ").split()
    input_numbers = list(map(int, input_numbers))
except ValueError:
    print("Invalid input. Please enter a valid list of integers separated by spaces.")
    exit()

def triple_number(num):
    return num * 3

tripled_numbers = list(map(triple_number, input_numbers))

print("Original List:", input_numbers)
print("Tripled List:", tripled_numbers)
