def process_file():
    # Asking user to input file.
    input_file = input("Enter the name of the file to read: ")
    output_file = input("Enter the name of the output file: ")

    try:
        # Opening and reading the file.
        with open(input_file, 'r') as f:
            content = f.read()
        
        # Process the content (convert to uppercase in this example)
        modified_content = content.upper()
        
        # Writing an output file.
        with open(output_file, 'w') as f:
            f.write("I love Python")
        
        print(f"Modification of {output_file} sucessful")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied. Cannot read '{input_file}' or write to '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    process_file()