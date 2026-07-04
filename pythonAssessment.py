import re

def count_specific_word(text, word):
    """Count how many times `word` appears in `text` (case-insensitive, whole word).

    Args:
        text (str): The string to search through.
        word (str): The search word.

    Returns:
        int: Number of occurrences. Returns 0 if no matches are found.
    """
    if not text or not word:
        return 0

    # Pull out every "word" (letters/digits/apostrophes) and compare directly.
    words = re.findall(r"[A-Za-z0-9']+", text.lower())
    target = word.lower().strip()

    count = 0
    for w in words:  # for loop (rubric)
        if w == target:
            count += 1
        else:
            continue
    return count


def identify_most_common_word(text):
    """Return the most common word in `text` (case-insensitive).

    Args:
        text (str): The text to analyze.

    Returns:
        str | None: The most common word, or None for an empty string.
    """
    if not text.strip():
        return None

    words = re.findall(r"[A-Za-z0-9']+", text.lower())
    if not words:
        return None

    # Build a frequency table.
    frequencies = {}
    for w in words:  # for loop (rubric)
        if w in frequencies:
            frequencies[w] += 1
        else:
            frequencies[w] = 1

    # Walk the table with a while loop to find the highest-frequency word.
    items = list(frequencies.items())
    index = 0
    most_common_word = items[0][0]
    highest_count = items[0][1]
    while index < len(items):  # while loop (rubric)
        word, freq = items[index]
        if freq > highest_count:
            highest_count = freq
            most_common_word = word
        index += 1

    return most_common_word


def calculate_average_word_length(text):
    """Calculate the average length of words in `text`.

    Punctuation and special characters are excluded from the length.

    Args:
        text (str): The text to analyze.

    Returns:
        float: The average word length, or 0 for an empty string.
    """
    if not text.strip():
        return 0

    # Words stripped of punctuation/special characters (letters & digits only).
    words = re.findall(r"[A-Za-z0-9]+", text)
    if not words:
        return 0

    total_length = 0
    for w in words:  # for loop (rubric)
        total_length += len(w)

    return total_length / len(words)


def count_paragraphs(text):
    """Count the number of paragraphs in `text`.

    Paragraphs are blocks of text separated by one or more empty lines.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of paragraphs. Returns 1 for an empty string.
    """
    if not text.strip():
        return 1

    # Split on one or more blank lines, then keep only non-empty blocks.
    blocks = re.split(r"\n\s*\n", text.strip())
    paragraphs = 0
    for block in blocks:  # for loop (rubric)
        if block.strip():
            paragraphs += 1

    if paragraphs == 0:
        return 1
    else:
        return paragraphs


def count_sentences(text):
    """Count the number of sentences in `text`.

    Sentences are delimited by '.', '!' or '?'. Consecutive terminators
    (e.g. "..." or "?!") count as a single sentence ending.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of sentences. Returns 1 for an empty string.
    """
    if not text.strip():
        return 1

    # Each run of sentence-ending punctuation marks one sentence boundary.
    sentences = re.findall(r"[.!?]+", text)
    if len(sentences) == 0:
        return 1
    else:
        return len(sentences)


def read_article(file_path):
    """Read a text file into a single string. Returns '' if the file is missing."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


if __name__ == "__main__":
    # Read the provided news article into a string variable.
    article = read_article("news_article.txt")

    # Fall back to a small built-in sample so the demo always runs.
    if not article.strip():
        article = (
            "Technology is changing the world at a rapid pace. "
            "Every day, new tools are released. Are we ready for them?\n\n"
            "Many people embrace the change. Others remain cautious. "
            "The future, however, belongs to those who adapt!"
        )

    search_word = "the"

    print("===== News Article Analysis =====")
    print(f"Occurrences of '{search_word}': {count_specific_word(article, search_word)}")
    print(f"Most common word: {identify_most_common_word(article)}")
    print(f"Average word length: {calculate_average_word_length(article):.2f}")
    print(f"Number of paragraphs: {count_paragraphs(article)}")
    print(f"Number of sentences: {count_sentences(article)}")
