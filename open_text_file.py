# Documentation: https://docs.python.org/3/library/functions.html#open

# Read text file to get contents
with open('input.txt', 'r') as file:
    contents = file.read()

# Processing of file contents can occur here
new_line = "New line contents"
output = contents + "\n" + new_line

# Write output to new text file (or overwrite if it already exists)
with open('output.txt', 'w') as file:
    file.write(output)

