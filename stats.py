def count_words(text):
    return len(text.split())

def count_characters(text):
    lower_text = text.lower()
    character_count_dict = {}
    for char in lower_text:
        if char in character_count_dict:
            character_count_dict[char] += 1
        else:
            character_count_dict[char] = 1
    return character_count_dict

def sorted_dict_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({char:dict[char]})
    sorted_list.sort(reverse=True,key=lambda d: list(d.values())[0])
    return sorted_list