#!/usr/bin/python3
"""script that prints stat of formatted input through stdin"""


def print_stats(status_codes, file_size):
    """prints the collected stats in a certain format"""
    print('File size: {}'.format(file_size))
    keys = sorted(status_codes)
    for key in keys:
        print('{}: {}'.format(key, status_codes[key]))


if __name__ == '__main__':
    import sys

    file_size = 0
    status_codes = {}
    count = 0
    available_stats = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(status_codes, file_size)
                count = 0

            count += 1
            line_splitted = line.split()
            try:
                file_size += int(line_splitted[-1])
            except [IndexError, ValueError]:
                pass

            try:
                if line_splitted[-2] in available_stats:
                    if status_codes.get(line_splitted[-2], -1) == -1:
                        status_codes[line_splitted[-2]] = 1
                    else:
                        status_codes[line_splitted[-2]] += 1
            except IndexError:
                pass

        print_stats(status_codes, file_size)

    except KeyboardInterrupt:
        print_stats(status_codes, file_size)
        raise
