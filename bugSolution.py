def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if sum(numbers) == 0:
        return 0  #Handle the case of all zeros
    return sum(numbers) / len(numbers)

# Example usage
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [0, 0, 0, 0, 0]
average = calculate_average(my_numbers) 
print(f"The average is: {average}")

my_numbers = [10, 20, 0, 40, 50]
average = calculate_average(my_numbers) 
print(f"The average is: {average}") 