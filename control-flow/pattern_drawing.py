# pattern_drawing.py

# Prompt the user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# Use while loop for rows
while row < size:
    # Use for loop for columns within each row
    for col in range(size):
        print("*", end="")
    
    # Move to the next line after completing a row
    print()
    
    # Increment row counter
    row += 1
