def count_words(path_to_book):
    
    with open(path_to_book) as f:
        book_content = f.read()
        book_words = book_content.split()
        print(f"Found {len(book_words)} total words")


def analyze_book(path_to_book):

    def sort_on(items):
        return items["count"]

    with open(path_to_book) as f:
        set_of_chars = set()
        analyzation_dict = None

        book_content = f.read()
        book_words = book_content.split()
        book_chars = []

        # create a set of unique chars
        for word in book_words:
            # book_chars.append(list(word))
            # print(list(word))
            for char in list(word):
                char_to_lower = char.lower()
                book_chars.append(char_to_lower)
                set_of_chars.add(char_to_lower)

        # print(book_chars)
        # print(set_of_chars)

        # {a:0, b:0, ... }
        analyzation_dict = dict.fromkeys(set_of_chars, 0)

        for char in book_chars:
            analyzation_dict[char] += 1

        # print(list(analyzation_dict))

        analyzation_list = []

        for key in analyzation_dict:
            analyzation_list.append({"char": key, "count": analyzation_dict[key]})

        result = sorted(analyzation_list, key=sort_on, reverse=True)
        # print(result)
        
        for i in range(0, len(analyzation_list)): 
            print(f'{result[i]["char"]}: {result[i]["count"]}')
