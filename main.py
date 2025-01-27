def main():
    with open("books/frankenstein.txt")  as buch:
        file_contents = buch.read()
        lower_file = file_contents.lower()
        wort_zahl = len(file_contents.split())
        print(wort_zahl, " words found in the document")
        char_count = {}
        for buchstaben in lower_file:
            if buchstaben in char_count:
                char_count[buchstaben] += 1
            else:
                char_count[buchstaben] = 1
        sort_char_count = dict(sorted(char_count.items(), key=lambda item:item[1], reverse=True))
        for entrys in sort_char_count:
            if entrys.isalpha():
                print(f"The '{entrys}' character was found {sort_char_count[entrys]} times")

main()