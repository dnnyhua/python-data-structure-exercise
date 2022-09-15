def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

    first_and_last=[]

    for name in people:
        combine_first_last = name['first'] + " " +  name['last']
        first_and_last.append(combine_first_last)
    
    return first_and_last


# Springboard's answer

# return [f"{person['first']} {person['last']}" for person in people]