"""
Step 1: Introduction to Basic Concepts
This module introduces fundamental Python concepts.
"""

# ============================================================================
# SECTION 1: IMPORTS
# ============================================================================
# Import necessary modules here
import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hangman_words import word_list

# ============================================================================
# SECTION 2: CONSTANTS
# ============================================================================
# Define constants here
# Example: MAX_VALUE = 100

# ============================================================================
# SECTION 3: HELPER FUNCTIONS
# ============================================================================
def placeholder_function(selected_word):
    """
    A placeholder function to demonstrate structure.    
    Returns:
        str: A placeholder message  
    """
    global placeholder
    length = len(selected_word)
    print(f"Length of the selected word: {length}")
    
    for _ in range(length):
        placeholder += "_"   
    
    print(placeholder)
    
    return "Helper function executed"


# ============================================================================
# SECTION 4: MAIN FUNCTION
# ============================================================================
def main():
    """
    Main function - Entry point of the program.
    """
    global placeholder
    selected_word = random.choice(word_list)
    print(f"Selected word: {selected_word}")   
    print(f"Word length: {len(selected_word)}")
    print()
    
    # Initialize variables
    length = len(selected_word)
    placeholder = "_" * length
    guesses = 0
    correct_guesses = []
    incorrect_guesses = []
    max_attempts = length + 5
    
    print(f"Placeholder: {placeholder}")
    print()
    
    # Game loop
    while True:
        guess = input("guess a letter: ").lower()
        guesses += 1
        
        # Check if letter was already guessed
        if guess in correct_guesses or guess in incorrect_guesses:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue
        
        # Check if guess is correct
        if guess in selected_word.lower():
            correct_guesses.append(guess)
            print(f"Correct! '{guess}' is in the word.\n")
        else:
            incorrect_guesses.append(guess)
            print(f"Sorry! '{guess}' is not in the word.\n")
        
        # Update placeholder display
        placeholder = ""
        for letter in selected_word:
            if letter.lower() in correct_guesses:
                placeholder += letter
            else:
                placeholder += "_"
        
        print(f"Placeholder: {placeholder}")
        print(f"Incorrect guesses: {', '.join(incorrect_guesses) if incorrect_guesses else 'None'}")
        print(f"Attempts used: {guesses}/{max_attempts}\n")
        
        # Check win condition
        if placeholder.lower() == selected_word.lower():
            print(f"Congratulations! You've guessed the word '{selected_word}' in {guesses} attempts!")
            break
        
        # Check lose condition
        if guesses >= max_attempts:
            print(f"Too many attempts! The word was '{selected_word}'. Better luck next time!")
            break
   


# ============================================================================
# SECTION 5: SCRIPT EXECUTION
# ============================================================================
if __name__ == "__main__":
    main()
