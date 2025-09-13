# Program to read a text file line by line and store each line in a list

def read_file_to_list(filename):
    lines_list = []                      # Initialize an empty list
    try:
        with open(filename, 'r') as file:
            # Read each line, strip newline characters, and add to list
            lines_list = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return lines_list                     # Return the list of lines


# Main program
filename = r"C:\Users\admin\Downloads\example.txt"  # File path
lines = read_file_to_list(filename)                 # Call the function

print("Contents of the file as a List:")
print(lines)                                       # Display the list
