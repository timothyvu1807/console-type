import random
import requests

API_Key = ""
word_list = []

def fetch_words_from_api():
    url = "https://api.wordnik.com/v4/words.json/randomWords?limit=10&api_key=" + API_Key
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return list(set([word['word'] for word in data]))  # Remove duplicates, if any
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def generate_word():
    if not word_list:
        print("No words available.")
        return None
    return word_list.pop(random.randint(0, len(word_list) - 1))  # Randomly pick and remove word

def main():
    global word_list
    word_list = fetch_words_from_api()
    
    if not word_list:
        print("Failed to fetch words from API.")
        return
    
    while word_list:
        word = generate_word()
        
        if word is None:
            return

        print(f"Spell this word: {word}")
        
        user_input = input("").strip()
        
        if user_input == '#':
            print("Exiting the program.")
            break
        
        if user_input.lower() == word.lower():
            print("Correct!")
        else:
            print(f"Incorrect!")

if __name__ == "__main__":
    main()