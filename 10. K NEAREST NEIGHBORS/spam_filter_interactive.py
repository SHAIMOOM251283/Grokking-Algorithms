class NaiveBayesClassifier:
    def __init__(self):
        self.spam_word_probabilities = {}
        self.not_spam_word_probabilities = {}

    def train(self, training_data):
        spam_count = 0
        not_spam_count = 0
        spam_word_counts = {}
        not_spam_word_counts = {}

        for subject, label in training_data:
            words = subject.lower().split()
            for word in words:
                if label == 'SPAM':
                    spam_word_counts[word] = spam_word_counts.get(word, 0) + 1
                    spam_count += 1
                else:
                    not_spam_word_counts[word] = not_spam_word_counts.get(word, 0) + 1
                    not_spam_count += 1

        total_words = len(spam_word_counts) + len(not_spam_word_counts)

        for word, count in spam_word_counts.items():
            self.spam_word_probabilities[word] = count / spam_count

        for word, count in not_spam_word_counts.items():
            self.not_spam_word_probabilities[word] = count / not_spam_count

    def predict(self, subject):
        spam_probability = 1.0
        not_spam_probability = 1.0

        for word in subject.lower().split():
            spam_probability *= self.spam_word_probabilities.get(word, 0.01)  # Smoothing
            not_spam_probability *= self.not_spam_word_probabilities.get(word, 0.01)  # Smoothing

        if spam_probability > not_spam_probability:
            return "SPAM"
        else:
            return "NOT SPAM"

def main():
    # Example training data
    training_data = [
        ("RESET YOU PASSWORD", "NOT SPAM"),
        ("YOU HAVE WON 1 MILLION DOLLARS", "SPAM"),
        ("SEND ME YOUR PASSWORD", "SPAM"),
        ("NIGERIAN PRINCE SENDS YOU 10 MILLION DOLLARS", "SPAM"),
        ("HAPPY BIRTHDAY", "NOT SPAM")
    ]

    classifier = NaiveBayesClassifier()
    classifier.train(training_data)

    while True:
        email_subject = input("Enter email subject (or type 'quit' to exit): ")
        if email_subject.lower() == 'quit':
            break
        prediction = classifier.predict(email_subject)
        print("Prediction:", prediction)

if __name__ == "__main__":
    main()
