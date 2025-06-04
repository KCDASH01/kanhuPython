# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Extract the first five elements
first_five = numbers[:5]

# Reverse the extracted elements
reversed_five = first_five[::-1]

# Print the results
print(f"original list: {numbers}")
print("extracted first five elements: {}".format(first_five))
print("reversed extracted elements: {}".format(reversed_five))
