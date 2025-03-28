import sys
from stats import print_report

# Read File function
def get_book_text(path_to_file):
    # open a file
    with open(path_to_file, encoding="UTF-8") as f:
        # contents of the file
        return f.read()
        
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    print_report(filepath, file_contents)

if __name__ == "__main__":
    main()