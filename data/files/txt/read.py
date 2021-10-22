def display_char(file_path,numb_chars):
    with open(file_path) as file:
        data = file.read(numb_chars)
        print(data)
def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print (data)
def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)
def run():
    display_char("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run()