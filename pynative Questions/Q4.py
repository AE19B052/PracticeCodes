'''
Write a program to remove characters from a string starting from zero up to n and return a new string.
For example:
    remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
    
    remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
'''
def remove_chars(word,n):
    print(f"Orginal String was {word} and number of elements removed for starting of string are {n}")
    a = word[n:]
    word = a
    return word

print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))