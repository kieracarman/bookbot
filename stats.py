def count_words(text):
    return len(text.split())

def count_chars(text):
    char_totals = {}

    for c in text:
        c = c.lower()
        if c not in char_totals:
            char_totals[c] = 1
        else:
            char_totals[c] += 1

    return char_totals

def sort_on(items):
    return items["num"]

def sort_chars(char_totals):
    sorted_list = []
    
    for c in char_totals:
        sorted_list.append({"char": c, "num": char_totals[c]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
