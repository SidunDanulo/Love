def popular_words(text, words):
    text_words = text.lower().split()
    result = {word: text_words.count(word) for word in words}

    return result
text = '''When I was One
I had just begun
When I was Two
I was nearly new'''

words = ['i', 'was', 'three', 'near']

print(popular_words(text, words))