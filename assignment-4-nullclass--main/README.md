# Task 4: Create a feature to throw an error if we enter the wrong word . For example if we enter a word which is not available the program should throw an error saying like this “word is not available” and provide some suggestion related to the word which is incorrect . If the user enter continuously 2 wrong word it should show list of wrong words which we enter so far in the error notification as well as it should give some suggestions related with wrong word .

## Overview
This task implements error-handling for unavailable words and provides suggestions. If a word is not available, the program suggests similar words and tracks the wrong words entered by the user.

## Model
- The model uses a sequential architecture for translation.
- Error-handling features and suggestions are implemented using difflib.

## Data
- Data consists of French-Tamil translation pairs.
- Sentences are preprocessed and tokenized.

## Files
- `task4.ipynb`: Contains the translation model and error-handling logic.
- `gui.py`: GUI script to interact with the model.

## Setup
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd <repo_name>
