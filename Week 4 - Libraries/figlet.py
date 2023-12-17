from pyfiglet import Figlet
import sys
import random



def main():
    preSetFonts = ["3-d", "3x5", "5lineoblique", "acrobatic", "alligator", "alligator2", "alphabet", "avatar",
        "banner", "banner3-D", "banner3", "banner4", "barbwire", "basic", "bell", "big",
        "bigchief", "binary", "block", "bubble", "bulbhead", "calgphy2", "caligraphy", "catwalk",
        "chunky", "coinstak", "colossal", "computer", "contessa", "contrast", "cosmic", "cosmike",
        "cricket", "cursive", "cyberlarge", "cybermedium", "cybersmall", "diamond", "digital", "doh",
        "doom", "dotmatrix", "drpepper", "eftichess", "eftifont", "eftipiti", "eftirobot", "eftitalic",
        "eftiwall", "eftiwater", "epic", "fender", "fourtops", "fuzzy", "goofy", "gothic",
        "graffiti", "hollywood", "invita", "isometric1", "isometric2", "isometric3", "isometric4", "italic",
        "ivrit", "jazmine", "jerusalem", "katakana", "kban", "larry3d", "lcd", "lean",
        "letters", "linux", "lockergnome", "madrid", "marquee", "maxfour", "mike", "mini",
        "mirror", "mnemonic", "morse", "moscow", "nancyj-fancy", "nancyj-underlined", "nancyj", "nipples",
        "ntgreek", "o8", "ogre", "pawp", "peaks", "pebbles", "pepper", "poison",
        "puffy", "pyramid", "rectangles", "relief", "relief2", "rev", "roman", "rot13",
        "rounded", "rowancap", "rozzo", "runic", "runyc", "sblood", "script", "serifcap",
        "shadow", "short", "slant", "slide", "slscript", "small", "smisome1", "smkeyboard",
        "smscript", "smshadow", "smslant", "smtengwar", "speed", "stampatello", "standard", "starwars",
        "stellar", "stop", "straight", "tanja", "tengwar", "term", "thick", "thin",
        "threepoint", "ticks", "ticksslant", "tinker-toy", "tombstone", "trek", "tsalagi", "twopoint",
        "univers", "usaflag", "wavy", "weird"
    ]
    while True:
        try:
            if len(sys.argv) == 1:
                givenFont = random.choice(preSetFonts)
                convert(givenFont)
                break
            elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font") and sys.argv[2] in preSetFonts:
                convert(sys.argv[2])
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid usage")
            sys.exit()

def convert(givenFont):
    toChange = input("Input: ")
    f = Figlet(font = givenFont)
    print(f.renderText(toChange))
    print(givenFont)



main()