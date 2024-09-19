def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    lowered_text = lower_text(text)
    characters = count_characters(lowered_text)
    list_of_dicts = [{'letter': letter, 'count': count} for letter, count in characters.items()]
    print(f"{num_words}")
    #print(f"{lowered_text}")
    #print(f"{characters}")  
    list_of_dicts.sort(reverse=True, key=get_count)
    for char_dict in list_of_dicts:
       letter = char_dict["letter"]
       count = char_dict["count"]
       print(f"The letter'{letter}' was found {count} times")
         
    
def get_book_text(path):    
    with open(path) as f:
        return f.read()
        
def count_words(text):
    words = text.split()
    return len(words)

def lower_text(text):
    return text.lower()

def count_characters(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    return char_count

def get_count(item):
    return item["count"]


main()

