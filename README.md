# News Article Text Analyzer

A small Python toolkit that performs natural language processing (NLP) style
text analysis on a news article. It was built for the **Summative Lab: Analyze
a News Article** assessment.

## Overview

The program reads a news article from a text file into a string and reports five
insights about its content:

1. How many times a specific word is used
2. The most common word
3. The average length of words
4. The number of paragraphs
5. The number of sentences

## Project Structure

```
Module4/
├── pythonAssessment.py   # Main script with all analysis functions
├── news_article.txt      # The article to analyze
└── README.md             # This file
```

## Requirements

- Python 3.6 or newer
- No external libraries (uses only the standard library `re` module)

## Usage

1. (Optional) Place the article you want to analyze in a file named
   `news_article.txt` in the same folder as `pythonAssessment.py`.
   If the file is missing, the script falls back to a small built-in sample.

2. Run the script:

   ```bash
   python3 pythonAssessment.py
   ```

3. Example output:

   ```
   ===== News Article Analysis =====
   Occurrences of 'the': 54
   Most common word: the
   Average word length: 5.22
   Number of paragraphs: 19
   Number of sentences: 48
   ```

## Functions

| Function | Arguments | Returns | Empty-string edge case |
|---|---|---|---|
| `count_specific_word(text, word)` | text to search, search word | `int` count (case-insensitive, whole word) | returns `0` when no match |
| `identify_most_common_word(text)` | text | `str` most common word | returns `None` |
| `calculate_average_word_length(text)` | text | `float` average word length (punctuation excluded) | returns `0` |
| `count_paragraphs(text)` | text | `int` paragraph count (split on blank lines) | returns `1` |
| `count_sentences(text)` | text | `int` sentence count (`.`, `!`, `?`) | returns `1` |

## How the Code Works

The whole script relies on Python's built-in `re` (regular expression) module to
pull words and punctuation out of the raw text. Here is what each function does,
step by step.

### `count_specific_word(text, word)`

Counts how many times a word appears, ignoring capitalisation.

1. If either `text` or `word` is empty, it returns `0` immediately.
2. `re.findall(r"[A-Za-z0-9']+", text.lower())` breaks the lower-cased text into
   a list of "words" (runs of letters, digits, or apostrophes). This strips away
   commas, periods, and quotes so they don't stick to a word.
3. A **`for` loop** walks every word and, using an **`if/else`**, adds `1` to the
   counter each time the word matches the target exactly.
4. Because it compares whole words, `"the"` inside `"theater"` is *not* counted.

### `identify_most_common_word(text)`

Finds the word that appears most often.

1. Returns `None` if the text is blank.
2. Splits the text into words the same way as above.
3. Builds a **frequency dictionary** (`{word: count}`) with a `for` loop — if a
   word is already a key it increments it, otherwise it adds it.
4. Uses a **`while` loop** to step through the dictionary and keep track of the
   word with the highest count, returning it at the end.

### `calculate_average_word_length(text)`

Returns the average number of characters per word.

1. Returns `0` for empty text.
2. `re.findall(r"[A-Za-z0-9]+", text)` grabs words made of letters and digits
   only (punctuation excluded, so it doesn't inflate the length).
3. A `for` loop sums the length of every word, then it divides that total by the
   number of words. Division in Python 3 returns a `float`.

### `count_paragraphs(text)`

Counts blocks of text separated by blank lines.

1. Returns `1` for empty text.
2. `re.split(r"\n\s*\n", text.strip())` splits the text wherever there is one or
   more blank lines — each remaining chunk is one paragraph.
3. A `for` loop counts only the non-empty chunks (an `if` skips blank ones).

### `count_sentences(text)`

Counts sentences by their ending punctuation.

1. Returns `1` for empty text.
2. `re.findall(r"[.!?]+", text)` finds every run of `.`, `!`, or `?`. The `+`
   means a run like `"..."` or `"?!"` is treated as a **single** sentence ending
   rather than several.
3. The number of matches is the number of sentences.

### `read_article(file_path)` and the `__main__` block

- `read_article` opens the file and returns its text, or an empty string if the
  file is missing (handled with `try`/`except FileNotFoundError`).
- The `if __name__ == "__main__":` block reads `news_article.txt`, falls back to
  a short built-in sample if that file is absent, then prints all five metrics.

> **Rubric constructs:** the script deliberately uses a `for` loop, a `while`
> loop, and `if/else` conditionals so every required construct is present.

## Importing the Functions

The analysis functions can also be imported and used in your own code:

```python
from pythonAssessment import count_specific_word, identify_most_common_word

text = "Python is fun. Python is powerful."
print(count_specific_word(text, "python"))   # 2
print(identify_most_common_word(text))        # "python"
```

The demonstration code only runs when the script is executed directly
(`if __name__ == "__main__":`), so importing the functions never triggers the
file read or printed output.

## Testing

Run the script directly to see the analysis on the sample (or your own) article.
Edge cases for empty input are handled as described in the table above.
