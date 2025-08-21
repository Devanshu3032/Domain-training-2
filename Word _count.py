# Program to count total words in a paragraph

# Predefined paragraph
paragraph = """Python is simple yet powerful.
Python is widely used in data science, machine learning,
and artificial intelligence. Python makes coding easier!"""

# Replace new lines with spaces
paragraph = paragraph.replace("\n", " ")

# Remove punctuation
for ch in [".", ",", "!", "?", ";", ":"]:
    paragraph = paragraph.replace(ch, "")

# Split into words
words = paragraph.split(" ")

# Remove empty strings
cleaned_words = []
for w in words:
    if w.strip() != "":
        cleaned_words.append(w)

# Count total words
total = len(cleaned_words)

print("Total words in paragraph:", total)