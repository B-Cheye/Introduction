string1 = input('Please enter the first string ')
string2 = input('Please enter the second string ')


def dup(srt_1: object, srt_2: object) -> object:
    """Args:
            two strings
       Returns:
             a list of characters that appear in both strings
    """
    duplicate = []

    for i in srt_1:
        for j in srt_2:
            if i == j:
                duplicate.append(i)
                break
    return set(duplicate)
print(dup(string1, string2))
