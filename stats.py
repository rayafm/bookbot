# Count Words function
def get_num_words(file_contents):

    words = file_contents.split()
    num_of_words = len(words)

    # print(f"{num_of_words} words found in the document")
    print(f"Found {num_of_words} total words")

# Count Characters function
def get_num_chars(file_contents):
    # lower text
    file_contents_lt = file_contents.lower() 

    # declare a dictionary
    dict = {}

    for w in file_contents_lt:
        for c in w:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1

    return dict

def sort_on(char_dict):
    return char_dict["count"]

def get_sortls_dict(file_contents):
    char_dict = get_num_chars(file_contents)
    char_count_ls = [{"character": key, "count": char_dict[key]} for key in char_dict if key.isalpha()]
    
    char_count_ls.sort(reverse=True, key=sort_on)

    for ch in char_count_ls:
        print(f"{ch["character"]}: {ch["count"]}")

def print_report(filepath, file_contents):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    get_num_words(file_contents)
    print("--------- Character Count -------")
    get_sortls_dict(file_contents)
    print("============= END ===============")