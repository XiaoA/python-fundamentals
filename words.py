def print_upper_words(words):
    """ Print one word per line, uppercased.

    print_upper_words(["I" "need" "a" "cup" "of" "coffee" "now"])
    I
    NEED
    A
    CUP 
    OF 
    COFFEE
    NOW

    """

    for word in words:
        print(word.upper())

print_upper_words(["I", "need", "a", "cup", "of", "coffee", "now"])
