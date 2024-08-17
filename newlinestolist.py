import json
fp = r"C:\Users\joehb\Documents\Coding\Personal-Python\Games\Toby Fox Saves Manager\Deltarune-Save-Manager\ch2_save"
with open(fp, "r", encoding="utf-8") as f:
    # Read each line of the file into a list
    lines = f.readlines()
    # Remove the newline character from each line
    lines = [line.strip() for line in lines]
    # Create a new list
    new_lines = []
    # Print each line
    for line in lines:
        new_lines.append([line])
    
    # Print the new list
    json.dump(new_lines, open("newlines.json", "w"), indent=4)