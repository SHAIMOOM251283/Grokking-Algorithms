class InvertedIndex:
    def __init__(self):
        self.index = {}

    def add_document(self, doc_id, text):
        words = text.split()
        for word in words:
            if word not in self.index:
                self.index[word] = set()
            self.index[word].add(doc_id)

    def search(self, query):
        query_words = query.split()
        result = None
        for word in query_words:
            if word in self.index:
                if result is None:
                    result = self.index[word]
                else:
                    result = result.intersection(self.index[word])
            else:
                return set()  # Return empty set if any word is not found
        return result


# Example usage:
if __name__ == "__main__":
    index = InvertedIndex()

    # Add some documents
    index.add_document(1, "hello world")
    index.add_document(2, "hello python")
    index.add_document(3, "python world")

    # Search for documents containing certain words
    print("Documents containing 'hello':", index.search("hello"))
    print("Documents containing 'world':", index.search("world"))
    print("Documents containing 'python':", index.search("python"))
    print("Documents containing 'hello' and 'world':", index.search("hello world"))
    print("Documents containing 'hello' and 'python':", index.search("hello python"))
    print("Documents containing 'python' and 'world':", index.search("python world"))
