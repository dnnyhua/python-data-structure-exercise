vowels = set('aeiou')

def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    phrase = phrase.lower()
    vowel_counter = {}
    
    for v in vowels:
        vowel_counter[v] = 0

    for char in phrase:
        if char in vowels:
            vowel_counter[char] += 1

    return vowel_counter       



# Springboard's answer
    # phrase = phrase.lower()
    # counter = {}

    # for ltr in phrase:
    #     if ltr in vowels:
    #         counter[ltr] = counter.get(ltr, 0) + 1

    # return counter