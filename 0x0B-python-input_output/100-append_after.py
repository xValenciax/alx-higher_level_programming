"""module defines append_after function"""


def append_after(filename="", search_string="", new_string=""):
    new_lines = []
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.find(search_string) != -1:
                new_lines.append(line)
                new_lines.append(new_string)
            else:
                new_lines.append(line)

    with open(filename, 'w', encoding='UTF-8') as f:
        f.writelines(new_lines)
