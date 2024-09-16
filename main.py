def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    lowered_text = lower_text(text)
    characters = count_characters(lowered_text)
    report_list = sort_dict(alphabet_dictionary)
    print(f"{num_words}")
    #print(f"{lowered_text}")
    print(f"{characters}")
    
  

def get_book_text(path):    
    with open(path) as f:
        return f.read()
        
def count_words(text):
    words = text.split()
    return len(words)

def lower_text(text):
    return text.lower()

def count_characters(lowered_text):
    letters = list(lowered_text)
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0
    
    for letter in letters:
        if letter == "a":
            a += 1
        elif letter == "b":
            b += 1
        elif letter == "c":
            c += 1
        elif letter == "d":
            d += 1
        elif letter == "e":
            e += 1
        elif letter == "f":
            f += 1
        elif letter == "g":
            g += 1
        elif letter == "h":
            h += 1
        elif letter == "i":
            i += 1
        elif letter == "j":
            j += 1
        elif letter == "k":
            k += 1
        elif letter == "l":
            l += 1
        elif letter == "m":
            m += 1
        elif letter == "n":
            n += 1
        elif letter == "o":
            o += 1
        elif letter == "p":
            p += 1
        elif letter == "q":
            q += 1
        elif letter == "r":
            r += 1
        elif letter == "s":
            s += 1
        elif letter == "t":
            t += 1
        elif letter == "u":
            u += 1
        elif letter == "v":
            v += 1
        elif letter == "w":
            w += 1
        elif letter == "x":
            x += 1
        elif letter == "y":
            y += 1
        elif letter == "z":
            z += 1
        else : 
            pass

    alphabet = ["a", 
                "b", 
                "c", 
                "d", 
                "e", 
                "f", 
                "g", 
                "h", 
                "i", 
                "j", 
                "k", 
                "l", 
                "m", 
                "n", 
                "o", 
                "p", 
                "q", 
                "r", 
                "s", 
                "t", 
                "u", 
                "v", 
                "w", 
                "x", 
                "y", 
                "z"
                ]
    alphabet_count = [a, 
                      b, 
                      c, 
                      d, 
                      e, 
                      f, 
                      g, 
                      h, 
                      i, 
                      j, 
                      k, 
                      l, 
                      m, 
                      n, 
                      o, 
                      p, 
                      q, 
                      r, 
                      s, 
                      t, 
                      u, 
                      v, 
                      w, 
                      x, 
                      y, 
                      z
                    ]

    
    
    alphabet_dictionary = dict(zip(alphabet, alphabet_count))
    return alphabet_dictionary

def sort_dict(alphabet_dictionary)
    return sort(alphabet_dictionary)       

main()
