import random

word_list = []

def fetch_words_from_file():
    """Fetch a list of words from the text file."""
    file_path = "larger_random_words.txt"  # Update the path as needed
    try:
        with open(file_path, "r") as file:
            words = file.readlines()
        return [word.strip() for word in words if word.strip()]  # Stripping newline characters
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def generate_word():
    """Function to randomly select a word from the list."""
    if not word_list:
        print("No words available.")
        return None
    return random.choice(word_list)

def main():
    global word_list
    word_list = fetch_words_from_file()
    
    if not word_list:
        print("Failed to fetch words from file.")
        return

    while True:
        # Generate a word
        word = generate_word()
        
        if word is None:
            return

        print(f"Spell this word: {word}")
        
        # Wait for the user's input
        user_input = input("").strip()
        
        # Check for the special character to exit
        if user_input == '#':
            print("Exiting the program.")
            break
        
        # Compare input with the random word, ignoring case
        if user_input.lower() == word.lower():
            print("Correct!")
        else:
            print(f"Incorrect!")

if __name__ == "__main__":
    main()