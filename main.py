def main():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()

    def count_words(text):
        text = file_contents.split()
        return len(text)
    num = count_words (file_contents)

    def count_letter(text):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        char_occurences = {}
        for char in alphabet:
            char_occurences[char] = text.lower().count(char)
        return char_occurences
    letters = count_letter (file_contents)
    
    def print_report():
        print("--- Estatistical Report of Frankenstein ---")
        print(f"{num} words were found in the document!")
        print("\n")
        for char in letters:
            print(f"The {char.upper()} character was found {letters[char]} times!")
    print_report()
        

main()