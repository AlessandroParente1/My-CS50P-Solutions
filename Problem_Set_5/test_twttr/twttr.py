import re

replacements = {
    'a': '',
    'e': '',
    'i': '',
    'o': '',
    'u': '',
    'A': '',
    'E': '',
    'I': '',
    'O': '',
    'U': '',
}

pattern = re.compile("|".join(re.escape(key) for key in replacements.keys()))

def main():
    word= input("Input: ")
    removed_vowels_word=shorten(word)

    print("Output: "+removed_vowels_word)



def shorten(word):
    return pattern.sub(lambda match: replacements[match.group(0)], word)


if __name__ == "__main__":
    main()
