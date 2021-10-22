def search(file_path):
    print("Searcing...")
    section = ""
    books ="Books:\n"
    with open(file_path) as file:
        for line in file:
            if line.startswith("Section"):
                section =+line
            else:git
                books =+ line
