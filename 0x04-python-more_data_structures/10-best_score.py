#!/usr/bin/python3
# AUTHORS Selim

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_score = -1
    best_score_key = ""
    for key, val in a_dictionary.items():
        if val >= best_score:
            best_score = val
            best_score_key = key
    return best_score_key if best_score != -1 else None
