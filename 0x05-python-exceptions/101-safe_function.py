#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except BaseException as base_err:
        sys.stderr.write('Exception: {}\n'.format(base_err))
        return None
    else:
        return res
