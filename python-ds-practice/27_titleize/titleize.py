def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """


    word_cap = []
    for word in phrase.split(' '):
        word = word.capitalize()
        word_cap.append(word)
    
    return ' '.join(word_cap)