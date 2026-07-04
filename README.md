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
├── news_article.txt      # (optional) The article to analyze
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
   Occurrences of 'the': 3
   Most common word: the
   Average word length: 4.67
   Number of paragraphs: 2
   Number of sentences: 6
   ```

## Functions

| Function | Arguments | Returns | Empty-string edge case |
|---|---|---|---|
| `count_specific_word(text, word)` | text to search, search word | `int` count (case-insensitive, whole word) | returns `0` when no match |
| `identify_most_common_word(text)` | text | `str` most common word | returns `None` |
| `calculate_average_word_length(text)` | text | `float` average word length (punctuation excluded) | returns `0` |
| `count_paragraphs(text)` | text | `int` paragraph count (split on blank lines) | returns `1` |
| `count_sentences(text)` | text | `int` sentence count (`.`, `!`, `?`) | returns `1` |

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
