import string

def most_frequent_word(paragraph):
    # Convert to lowercase
    paragraph = paragraph.lower()
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    paragraph = paragraph.translate(translator)
    # Split into words
    words = paragraph.split()
    # Count frequency
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    # Find the most frequent word
    if not freq:
        return None
    most_freq_word = max(freq, key=freq.get)
    return most_freq_word

if __name__ == "__main__":
    paragraph = input("Enter a paragraph: ")
    result = most_frequent_word(paragraph)
    print(result)
