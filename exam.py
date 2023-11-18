# Define the file name
file_name = 'text.txt'

# Initialize an empty variable to store file contents
file_contents = ""

# Open the file in read mode using a 'with' statement
with open(file_name, 'r') as file:
    # Read the file line-by-line and store the lines in the variable
    for line in file:
        file_contents += line  # Append each line to the variable

# Close the file (automatically handled by the 'with' statement)

# Display the file contents
print("File Contents:")
print(file_contents)
