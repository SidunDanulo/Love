import re

def first_word(text):
    """
    Повертає перше слово з рядка.
    Слово може містити апостроф. Ігноруються пробіли, крапки та коми.
    """
    match = re.search(r"[a-zA-Zа-яА-ЯїЇєЄіІґҐ']+", text)
    if match:
        return match.group(0)
    return ''
print(first_word("Haybob"))
print(first_word("...."))
print(first_word("  ,,,Привіт, як ти"))
print(first_word("one"))
print(first_word("jopa"))