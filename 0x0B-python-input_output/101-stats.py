#!/usr/bin/python3
"""script that prints stat of formatted input through stdin"""


def collect_stats(lines=[], status_codes={}, file_size=0):
    """collects stat from stdin lines"""
    available_stats = ['200', '301', '400', '401', '403', '404', '405', '500']
    for line in lines:
        lines_splitted = line.split(' ')

        try:
            file_size += int(lines_splitted[-1])
        except [IndexError, ValueError]:
            pass

        try:
            if lines_splitted[-2] in available_stats:
                if status_codes.get(lines_splitted[-2]):
                    status_codes[lines_splitted[-2]] += 1
                else:
                    status_codes[lines_splitted[-2]] = 1
        except IndexError:
            pass

    return file_size


def print_stats(status_codes={}, file_size=0):
    """prints the collected stats in a certain format"""
    keys = list(status_codes.keys())
    print('File size: {}'.format(file_size))
    for key in sorted(keys):
        print('{}: {}'.format(key, status_codes[key]))


if __name__ == '__main__':
    import sys

    file_size = 0
    status_codes = {}
    lines = []

    try:
        for line in sys.stdin:
            lines.append(line)
            if len(lines) == 10:
                file_size = collect_stats(lines, status_codes, file_size)
                print_stats(status_codes, file_size)
                lines.clear()
    except KeyboardInterrupt as e:
        file_size = collect_stats(lines, status_codes, file_size)
        print_stats(status_codes, file_size)
        raise
