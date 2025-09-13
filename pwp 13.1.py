def count_file_stats(filename):
    try:
        with open(filename, 'r') as file:    # Opens the file in read mode
            lines = file.readlines()         # Reads all lines into a list

            num_lines = len(lines)           # Counts the number of lines
            num_words = sum(len(line.split()) for line in lines)  # Counts words
            num_chars = sum(len(line) for line in lines)          # Counts characters

            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Number of characters: {num_chars}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")

# Run the program
count_file_stats(r"C:\Users\admin\Downloads\example.txt")
