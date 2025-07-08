def get_num_words(text):
    split_text = text.split()
    word_num = len(split_text)
    return word_num

def get_char_count(text):
    char_dict = {}
    word_list = text.split()
    for word in word_list:
        word = word.lower()
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def get_char_dicts(dict):
    dict_list = []
    for item in dict:
        if item.isalpha():
            char_dict = {"char": f'{item}', "num": dict[item]}
            dict_list.append(char_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


