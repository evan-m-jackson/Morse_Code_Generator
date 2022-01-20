dash = "———"
dot = "·"

morse_dict = {
    "a": f"{dot} {dash}",
    "b": f"{dash} {dot} {dot} {dot}",
    "c": f"{dash} {dot} {dash} {dot}",
    "d": f"{dash} {dot} {dot}",
    "e": f"{dot}",
    "f": f"{dot} {dot} {dash} {dot}",
    "g": f"{dash} {dash} {dot}",
    "h": f"{dot} {dot} {dot} {dot}",
    "i": f"{dot} {dot}",
    "j": f"{dot} {dash} {dash} {dash}",
    "k": f"{dash} {dot} {dash}",
    "l": f"{dot} {dash} {dot} {dot}",
    "m": f"{dash} {dash}",
    "n": f"{dash} {dot}",
    "o": f"{dash} {dash} {dash}",
    "p": f"{dot} {dash} {dash} {dot}",
    "q": f"{dash} {dash} {dot} {dash}",
    "r": f"{dot} {dash} {dot}",
    "s": f"{dot} {dot} {dot}",
    "t": f"{dash}",
    "u": f"{dot} {dot} {dash}",
    "v": f"{dot} {dot} {dot} {dash}",
    "w": f"{dot} {dash} {dash}",
    "x": f"{dash} {dot} {dot} {dash}",
    "y": f"{dash} {dot} {dash} {dash}",
    "z": f"{dash} {dash} {dot} {dot}",
    "0": f"{dash} {dash} {dash} {dash} {dash}",
    "1": f"{dot} {dash} {dash} {dash} {dash}",
    "2": f"{dot} {dot} {dash} {dash} {dash}",
    "3": f"{dot} {dot} {dot} {dash} {dash}",
    "4": f"{dot} {dot} {dot} {dot} {dash}",
    "5": f"{dot} {dot} {dot} {dot} {dot}",
    "6": f"{dash} {dot} {dot} {dot} {dot}",
    "7": f"{dash} {dash} {dot} {dot} {dot}",
    "8": f"{dash} {dash} {dash} {dot} {dot}",
    "9": f"{dash} {dash} {dash} {dash} {dot}",
    ".": f"{dot} {dash} {dot} {dash} {dot} {dash}",
    ",": f"{dash} {dash} {dot} {dot} {dash} {dash}",
    "?": f"{dot} {dot} {dash} {dash} {dot} {dot}",
    "'": f"{dot} {dash} {dash} {dash} {dash} {dot}",
    "!": f"{dash} {dot} {dash} {dot} {dash} {dash}",
    "/": f"{dash} {dot} {dot} {dash} {dot}",
    "(": f"{dash} {dot} {dash} {dash} {dot}",
    ")": f"{dash} {dot} {dash} {dash} {dot} {dash}",
    "&": f"{dot} {dash} {dot} {dot} {dot}",
    ":": f"{dash} {dash} {dash} {dot} {dot} {dot}",
    ";": f"{dash} {dot} {dash} {dot} {dash} {dot}",
    "=": f"{dash} {dot} {dot} {dot} {dash}",
    "+": f"{dot} {dash} {dot} {dash} {dot}",
    "-": f"{dash} {dot} {dot} {dot} {dot} {dash}",
    "_": f"{dot} {dot} {dash} {dash} {dot} {dash}",
    '"': f"{dot} {dash} {dot} {dot} {dash} {dot}",
    "$": f"{dot} {dot} {dot} {dash} {dot} {dot} {dash}",
    "@": f"{dot} {dash} {dash} {dot} {dash} {dot}",
}


class MorseCode:
    def __init__(self, text, morse_dict):
        self.text = text
        self.morse_dict = morse_dict

    def encode(self):
        result = ""
        for ch in self.text:
            if ch == " ":  # Spaces get a 4 character length space.
                result += "    "
            elif ch.lower() in self.morse_dict:
                result += self.morse_dict[ch.lower()]
            else:
                return f"Sorry {ch} cannot be converted to Morse Code."
            result += "   "  # Every charatcer gets a 3 character length space after.  So a space in original text would end up getting a 7 character space in the Morse Code.
        return result

    def get_morse_code(self, word):
        print(word)


# Project Start
print("WELCOME TO THE MORSE CODE TRANSALATOR!")
text = input("Please enter the text you want to encode: ")

morse = MorseCode(text, morse_dict)
code = morse.encode()
morse.get_morse_code(code)
