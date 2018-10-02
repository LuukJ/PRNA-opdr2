def decode(code):
    """
    Decodeert gecodeerde tekst.

    Ondersteunt tekst zoals gegeven door encode.
    Met een backslash is alles te 'escapen'

    TODO:
     - Het toevoegen van een accumulator.
     - Het toevoegen van herkenning van codewoorden :R en :P
     - Het toevoegen van verwerking van de codewoorden
    """
    out = ""
    i = 0
    n = 0
    prevletter=""
    wasdigit = False
    digits = ""
    escape = False
    while i < len(code):
        isescape=False
        char = code[i]
        if escape:
            n=int(digits or "1")
            escape=False
            out += n*prevletter
            prevletter = char
            i+=1
            continue
        if not escape and char.isdigit():
            digits += char
        elif char == "\\":
            isescape = True
        else:
            n = int(digits or "1")
            digits = ""
            escape = False
            out += n*prevletter
            prevletter = char
        wasdigit = char.isdigit() and not escape
        escape = isescape
        i += 1
    out += char
    return out
