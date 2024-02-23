import hashlib

class Simhash:
    def __init__(self, tokens, hashbits=64):
        self.hashbits = hashbits
        self.hash = self._simhash(tokens)

    def _simhash(self, tokens):
        v = [0] * self.hashbits
        for t in [self._string_hash(x) for x in tokens]:
            bitmask = 0
            for i in range(self.hashbits):
                bitmask = 1 << i
                if t & bitmask:
                    v[i] += 1
                else:
                    v[i] -= 1
        fingerprint = 0
        for i in range(self.hashbits):
            if v[i] >= 0:
                fingerprint += 1 << i
        return fingerprint

    def _string_hash(self, v):
        return int(hashlib.md5(v.encode('utf-8')).hexdigest(), 16)

    def similarity(self, other):
        x = (self.hash ^ other.hash) & ((1 << self.hashbits) - 1)
        ans = 0
        while x:
            ans += 1
            x &= x - 1
        return ans

if __name__ == "__main__":
    # Input documents from the user
    document1 = input("Enter the first document: ")
    document2 = input("Enter the second document: ")
    document3 = input("Enter the third document: ")

    # Tokenize the documents
    tokens1 = document1.split()
    tokens2 = document2.split()
    tokens3 = document3.split()

    # Create Simhash objects for the documents
    simhash1 = Simhash(tokens1)
    simhash2 = Simhash(tokens2)
    simhash3 = Simhash(tokens3)

    # Calculate and print the similarity between the documents
    print("Similarity between document1 and document2:", simhash1.similarity(simhash2))
    print("Similarity between document1 and document3:", simhash1.similarity(simhash3))
    print("Similarity between document2 and document3:", simhash2.similarity(simhash3))
