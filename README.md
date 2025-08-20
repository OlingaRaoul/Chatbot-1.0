# Chatbot-1.0
A simple, command-line based FAQ (Frequently Asked Questions) chatbot. It uses fuzzy string matching to find the best answer to a user's question from a predefined dictionary, making it robust to typos and variations in phrasing.

Features
Fuzzy Matching: Intelligently matches user input to the closest known question using the difflib library.

Typo Tolerance: Doesn't require perfect spelling or phrasing to find a relevant answer.

Simple & Lightweight: Easy to understand, modify, and extend with new Q&A pairs.

Command-Line Interface: Runs directly in your terminal.

How It Works
The core function, get_best_match, takes the user's input and compares it against a list of pre-defined questions.

It uses difflib.get_close_matches to find the closest match from the list.

The cutoff parameter (set to 0.6) controls how similar the user's input needs to be to a known question to trigger a match. A lower value makes the matcher more forgiving.

If a match is found above the similarity threshold, it returns the corresponding answer from the dictionary.

If no good match is found, it returns a friendly apology message.