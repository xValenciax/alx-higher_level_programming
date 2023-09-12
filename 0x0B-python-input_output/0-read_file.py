"""module that defines the read file function"""


def read_file(filename=""):
    content = ""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    print(content)
