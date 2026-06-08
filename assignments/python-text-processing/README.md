# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice working with strings, file I/O, and basic text cleanup in Python. By the end of this assignment, students will be able to read text from a file, transform it, and produce simple text-based results.

## 📝 Tasks

### 🛠️ Clean and Normalize Text

#### Description
Write a function that takes a string of text and prepares it for analysis by removing extra whitespace and standardizing the casing.

#### Requirements
Completed program should:

- Accept a string of text as input.
- Remove leading and trailing whitespace.
- Convert the text to lowercase.
- Replace repeated spaces with a single space.
- Example:
  ```python
  normalize_text("  Hello   World  ")
  # "hello world"
  ```

### 🛠️ Count Words in a File

#### Description
Write a function that reads text from a file and counts how many words it contains.

#### Requirements
Completed program should:

- Open and read a text file using Python.
- Use the cleaned text from the first task before counting words.
- Return the total number of words.
- Example:
  ```python
  count_words("sample.txt")
  # 42
  ```

### 🛠️ Build a Text Summary

#### Description
Write a function that creates a short summary of a text file, including the number of lines, words, and characters.

#### Requirements
Completed program should:

- Read the contents of a text file.
- Count the number of lines, words, and characters.
- Return the results in a clear, formatted string.
- Example:
  ```python
  summarize_text("sample.txt")
  # "Lines: 5, Words: 42, Characters: 230"
  ```