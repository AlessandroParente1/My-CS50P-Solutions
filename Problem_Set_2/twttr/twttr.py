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

word= input("Input: ")

result=pattern.sub(lambda match: replacements[match.group(0)], word)

print("Output: "+result)
