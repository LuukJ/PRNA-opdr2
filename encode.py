
"""Encodeerfunctie mbt unicode files"""
def encode(text):
    out = ""
    i = 0
    while i < len(text):
        n = 0
        char = text[i]
        while i < len(text) and text[i] == char:
            n += 1
            i += 1
        if char in "\\01234567890":
            out += "\\"
        out += char
        if n > 1:
            out += str(n)
    return out
