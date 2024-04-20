# File Creation
try:
    # Open "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("New line here\n")
except IOError as e:
    print("Error: Unable to create or write to the file.")
    print(e)
finally:
    print("File creation completed successfully.")

# File Reading and Display
try:
    # Open "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied while accessing the file.")
except Exception as e:
    print("Error:", e)
finally:
    print("File reading completed successfully.")

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("RAAVA line 2\n")
        file.write("12345\n")
        file.write("My name is idris\n")
except IOError as e:
    print("Error: Unable to append to the file.")
    print(e)
finally:
    print("File appending completed successfully.")
