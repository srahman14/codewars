def encode(st):
    coding = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
    return "".join(coding[c] if c in coding else c for c in st)

def decode(st):
    decoding = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u"}
    return "".join(decoding[c] if c in decoding else c for c in st)

