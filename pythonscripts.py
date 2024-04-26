# Specify the file name
file_name = "output.txt"

def write_to_file(text):
    with open(file_name, "a") as file:
        file.write(text + "\n")

def clean_last_line():
    with open(file_name, "r+") as file:
        lines = file.readlines()
        if lines:
            file.seek(0)
            file.truncate()
            file.writelines(lines[:-1])

print("Enter text (Type 'clean' to remove the last line, Press Enter to finish):")

while True:
    # Get input from the user
    input_text = input()
    
    # Check if the input is 'clean'
    if input_text.strip() == "clean":
        clean_last_line()
        print("Last line cleaned.")
    elif not input_text:
        break
    else:
        write_to_file(input_text)

print("Text written to", file_name)
