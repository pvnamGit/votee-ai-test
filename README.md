## Invite to Votee AI Code Test
### 1. Prerequistes
Befor running the script, ensure you have the following installed:
  1. Python 3.x
  2. `nltk` library
  3. Internet connection (for downloading NLTK words and interacting with the VOTEE API)

### Installation
  1. Install Python if you haven't already: [Python Download](https://www.python.org/downloads/release/python-3921/)
  2. Install the required libraries by running:
     ```bash
     pip install nltk requests
     ```
  3. Download the NLTK word corpus:
    ```python
      import nltk
       nltk.download("words")
    ```
### How to use
  1. Clone or download the script to your local machine
  2. Open a terminal and run the script:
    ```bash
      python main.py
    ```
### Usage example:
When running the script, you will be prompted to choose one of the floowing options:
  ```text
    Choose an option:
      1. Auto guess daily:
      2. Auto guess random:
      3. Auto guess word:
    Enter your choice:
  ```
#### Option 1: Auto Guessing Daily:
You will need to inout the size of the word (e.g: 5). The script will then make guesses and display the current pattern as it progresses
#### Option 2: Auto Guessing Random:
Enter the word size and a randome seed(to ensure the random gueesses are consitent accross different run), and the script will begining guessing.
#### Option 3: Auto Guessing Word:
Input the word you want to guess, and the script will automatically attempt to solve the word by makeing educated guesses.
