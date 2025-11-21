import string
from collections import Counter

def most_frequent_word(paragraph):
    # Convert to lowercase
    text = paragraph.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = text.split()
    # Count word frequencies
    freq = Counter(words)
    # Find the most common word
    if freq:
        most_common_word, _ = freq.most_common(1)[0]
        return most_common_word
    else:
        return ""

# Accept input and print output
if __name__ == "__main__":
    paragraph = input("Enter a paragraph: ")
    print(most_frequent_word(paragraph))