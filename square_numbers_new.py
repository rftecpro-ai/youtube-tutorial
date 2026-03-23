def square_numbers(numbers):
    """Returns a new list with each positive number squared, excluding negatives."""
    return [n ** 2 for n in numbers if n >= 0]

# Example usage
nums = [1, -2, 3, -4, 5]
print(square_numbers(nums))  # Output: [1, 9, 25]
