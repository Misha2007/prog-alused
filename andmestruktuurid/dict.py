"""Dictionary exercises."""


def get_hobbies(hobbies_dict: dict, name: str) -> list:
    """
    Return the hobbies of a given person.

    hobbies = {
    "Tom": ["running", "reading"],
    "John": ["movies", "music", "swimming"]
    }

    get_hobbies(hobbies, "Tom")  => ["running", "reading"]
    get_hobbies(hobbies, "Timmy")  => "name not in dictionary"

    :param hobbies_dict: dictionary with peoples' hobbies.
    :param name: name of person whose hobbies are to be returned.

    :return: List of hobbies of the person with given name or "name not in dictionary".
    """
    if name in hobbies_dict:
        return hobbies_dict[name]
    else:
        return "name not in dictionary"


def find_tallest(height_dict: dict) -> str:
    """
    Return the name of the tallest peron in given dictionary.

    find_tallest({"Tom": 186, "Mari": 175, "Jhon": 190}) => "Jhon"

    :param height_dict: dictionary with peoples' names and heights
    :return name of tallest person in given dict.
    """
    height_list = sorted(list(height_dict.values()))
    height = height_list[-1]
    return list(height_dict.keys())[list(height_dict.values()).index(height)]


def remove_sixes(six_dict: dict) -> dict:
    """
    Return a dictionary where all keys which's values are dividable by six are removed.

    remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18}) => {"a": 4, "b": 8}

    :param six_dict: dictionary to be modified.
    :return: dict without values that are dividable by six.
    """
    for k in list(six_dict.keys()):
        if six_dict[k] % 6 == 0:
            del six_dict[k]
    return six_dict


def exchange_keys_and_values(exchange_dict: dict) -> dict:
    """
    Return a dict where keys and values have been exchanged.

    exchange_keys_and_values({"a": "b", "c": "d"}) => {"b": "a", "d": "c"}

    :param exchange_dict: dictionary to be modified.
    :return dictionary where values and keys have been exchanged.
    """
    exchange_dict = {v: k for k, v in exchange_dict.items()}

    return exchange_dict


def count_symbol_appearances(stringy: str) -> dict:
    """
    Return dict where key is the symbol and the value is the count this symbol is present in the string.

    count_symbol_appearances("hello hi") => {'h': 2, 'e': 1, 'l': 2, 'o': 1, ' ': 1, 'i': 1}

    :param stringy: string to be processed.
    :return: dictionary with symbol counts.
    """
    dict_str = {}
    for i in range(len(stringy)):
        dict_str[stringy[i]] = stringy.count(stringy[i])
    return dict_str


def organise_by_first_symbol(strings: list) -> dict:
    """
    Return dict where key the is a symbol and the value is a list of words starting with this symbol.

    organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]) =>
        {'h': ['hello'], 'w': ['word', 'world', 'welcome'], 'y': ['yes']}

    :param strings: list of strings.
    :return: dict with starting symbol and corresponding words in order of appearance.
    """
    dict_list = {}
    for i in range(len(strings)):
        if strings[i][0] in dict_list.keys():
            dict_list[strings[i][0]].append(strings[i])
        else:
            dict_list[strings[i][0]] = [strings[i]]
    return dict_list
 
hobbies = {
    "Tom": ["running", "reading"],
    "John": ["movies", "music", "swimming"]
    }
print(get_hobbies(hobbies, "Timmy"))

print(find_tallest({"Tom": 186, "Mari": 175, "Jhon": 190}))

print(remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18}))

print(exchange_keys_and_values({"a": "b", "c": "d"}))

print(count_symbol_appearances("hello hi"))

print(organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]))