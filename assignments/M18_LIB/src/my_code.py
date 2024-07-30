import re

def ispal(s):

    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

def testPalindrome(f):

    test_cases = [
        ("hello", False),
        ("", True), 
        ("saippuakauppias", True),
        ("moi1iom", True),
    ]

    for s, expected in test_cases:
        if f(s) != expected:
            return False
    
    return True

if __name__ == '__main__':
    rc = testPalindrome(ispal)
    print(rc)


"""
Kirjoita testifunktio testPalindrome(f) joka testaa funktion
f(s) toimintaa. Funktion f tulee palauttaa True jos s on
palindromi ja False muuten. Funktio f tulee jättää välimerkit ja
välilyönnit huomioimatta. Samoin isot ja pienet kirjaimet ovat
samanarvoisia1. Vastaavasti testPalindrome palauttaa True jos
f toimii oikein ja muuten False. Huomaa, ett¨a jos merkkijonossa
s on 0 tai 1 merkki¨a, on se palindromi.
"""