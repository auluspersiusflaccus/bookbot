def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    lowered_text = lower_text(text)
    print(f"{num_words}")
    print(f"{lowered_text}")
  

def get_book_text(path):    
    with open(path) as f:
        return f.read()
        
def count_words(text):
    words = text.split()
    return len(words)

def lower_text(text):
    return text.lower()

#def count_characters(lowered_text)

main()
