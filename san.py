def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text

print(correct_sentence("hello world"))
print(correct_sentence("Hello world."))
print(correct_sentence("already correct."))
print(correct_sentence("this is fine"))