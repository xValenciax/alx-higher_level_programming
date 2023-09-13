#!/usr/bin/python3

import sys
import os


def collect_stats(lines=[], status_codes={}, file_size=0):
    for line in lines:
        lines_splitted = line.split(' ')
        file_size += int(lines_splitted[-1])
        if status_codes.get(lines_splitted[-2]):
            status_codes[lines_splitted[-2]] += 1
        else:
            status_codes[lines_splitted[-2]] = 1
    return file_size


def print_stats(status_codes={}, file_size=0):
    keys = list(status_codes.keys())
    sys.stdout.write(f'File size: {file_size}\n')
    for key in keys:
        sys.stdout.write(f'{key}: {status_codes[key]}\n')


try:
    file_size = 0
    status_codes = {}
    lines = []
    while True:
        lines.append(sys.stdin.readline())
        if len(lines) == 10:
            file_size = collect_stats(lines, status_codes, file_size)
            print_stats(status_codes, file_size)
            lines.clear()
except KeyboardInterrupt as e:
    pass

file_size = collect_stats(lines, status_codes, file_size)
print_stats(status_codes, file_size)
