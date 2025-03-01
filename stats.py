def count_words(text):
    word_count = len(text.split())
    return word_count

def count_characters(text):
    lower_text = text.lower()
    character_count = {}
    for char in lower_text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sorted_dict_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({char:dict[char]})
    sorted_list.sort(reverse=True,key=lambda d: list(d.values())[0])
    return sorted_list