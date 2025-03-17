def count_words(text):
    return len(text.split())

def count_characters(text):
    num_characters = {}
    lowercased = text.lower()
    for c in set(lowercased):
        num_characters[c] = lowercased.count(c)
    return num_characters

def sort_on(dict):
    return dict["count"]

def char_count_sorted(num_chars):
    chars_sorted = []

    for char in num_chars:
        #print(f"key={char}, value={num_chars[char]}")
        chars_sorted.append({"character":char,"count":num_chars[char]})

    chars_sorted.sort(reverse=True,key=sort_on)
    #print(chars_sorted)
    return chars_sorted