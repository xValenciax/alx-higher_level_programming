#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv.copy()[1:]
    len = len(args)
    args_str = "arguments:"

    if len == 1:
        args_str = "argument:"

    if len == 0:
        args_str = "arguments."

    print(f"{len} {args_str}")

    for i, arg in enumerate(args):
        print(f"{i + 1}: {arg}")
