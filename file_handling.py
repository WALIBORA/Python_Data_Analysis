filename = input("Enter the name of the file to read: ")
try:
    with open(filename, "r") as infile:
        content = infile.read()
    modified_content = content.upper()
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("Success! Modified content has been written to 'output.txt'.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
