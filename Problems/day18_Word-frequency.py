
def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


text = "hello world hello"
frequency = word_frequency(text)
print(frequency)  # Output: {'hello': 2, 'world': 1}