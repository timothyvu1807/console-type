# import random
# import requests

# API_Key = "h3z9q8v2r1w4o0xg7y5jklm6abc7def8n9stuvw4r12g3p0yz"
# API_License = "N5M8O-KJ4G1-LB2E3-F6A7D-H9I0"
# word_list = []

# def fetch_words_from_api():
#     """Fetch a list of words from the API"""
#     url = ""
#     headers = {
#         "Authorization": f"Bearer {API_Key}",
#         "License": API_License
#     }
#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()  # Raises an HTTPError for bad responses
#         data = response.json()  # Assuming the API returns a JSON response with a list of words
#         return data.get('words', [])  # Adjust based on the actual response structure
#     except requests.RequestException as e:
#         print(f"An error occurred: {e}")
#         return []

# def generate_word():
#     """Function to randomly select a word from the list"""
#     if not word_list:
#         print("No words available.")
#         return None
#     return random.choice(word_list)

# def main():
#     global word_list
#     word_list = fetch_words_from_api()
    
#     if not word_list:
#         print("Failed to fetch words from API.")
#         return

#     # Generate a word
#     word = generate_word()
    
#     if word is None:
#         return

#     print(word)
    
#     # Wait for the user's input
#     user_input = input("").strip().lower()
    
#     # Compare input with the random word
#     if user_input == word:
#         print("Correct!")
#     else:
#         print("Incorrect! ")

# if __name__ == "__main__":
#     main()
# ^^^ my API key expired and i have to renew  it too frequently...
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