def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

#  use .replace(" ","") to get rid of spaces in between words
# .lower() to lowercase everything


    phrase_1 = phrase.lower().replace(" ","")
    
    return phrase_1 == phrase_1[::-1]
      