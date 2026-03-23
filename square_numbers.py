def square_numbers(numbers):
    """Returns a new list with each number squared."""
    return [n ** 2 for n in numbers]

# Example usage
nums = [1, 2, 3, 4, 5]
print(square_numbers(nums))  # Output: [1, 4, 9, 16, 25]
