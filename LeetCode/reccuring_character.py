def recurring_character(given_string: str):
    hash_map = {}
    for character in given_string:
        if character not in hash_map.keys():
            hash_map[character] = 1
            continue
        return character
    
print(recurring_character("AAAAAA"))
