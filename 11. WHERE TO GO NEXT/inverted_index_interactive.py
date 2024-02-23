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


def main():
    index = InvertedIndex()

    # Add some example documents
    index.add_document(1, "hello world")
    index.add_document(2, "hello python")
    index.add_document(3, "python world")

    print("Welcome to the Inverted Index Search!")
    print("Available commands:")
    print("- search [query]: Search for documents containing the specified query")
    print("- exit: Exit the program")

    while True:
        user_input = input("Enter a command: ").strip()

        if user_input.lower() == "exit":
            print("Exiting...")
            break

        elif user_input.lower().startswith("search"):
            query = user_input[len("search"):].strip()
            if query:
                results = index.search(query)
                if results:
                    print("Documents containing '{}': {}".format(query, results))
                else:
                    print("No documents found containing '{}".format(query))
            else:
                print("Please provide a query to search.")

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
